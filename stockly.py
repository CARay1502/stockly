import yfinance as yf
import streamlit as st
import pandas as pd 
from pandas_datareader import data as pdr
import requests 
from pathlib import Path

# --- PAGE CONFIG --- 
st.set_page_config(
    page_title="Stockly",
    page_icon="chart_with_upwards_trend",
    layout="centered",
)
# --- PATH SETTINGS & CSS FILE LOAD--- 
#current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#css_file = current_dir / "styles" / "main.css"
#with open(css_file) as f:
    #st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

yf.pdr_override()   #  NO IDEA WHAT THIS IS LOL

# --- LANDING PAGE --- 
st.subheader("Stock Data AI Aggregator! Relevant Data & News...") 

#--- SIDE BAR BIO --- 
with st.sidebar:
    st.header("Welcome to Stockly!")
    st.subheader("Investing made easy!") 
    st.write(
        """
        We are a FinTech startup located in Charlotte, NC. Devoted to making stock data & analysis easy and efficient!
        """
    )
    st.divider()
    st.caption("Navigate over to our Test Data Engine")

# Function to convert company name to its corresponding stock ticker
# --- Main st.form ---
with st.form("Stock Ticker Symbol Selector"):
    stockTicker = st.text_input("Enter the Stock Ticker Symbol here...") 
    submitted = st.form_submit_button("Get Data!") 
if submitted: 
    if not stockTicker:
        st.info("Please provide a valid Stock Ticker") 
        st.stop()

# --- NEWS API KEY --- 
api_key = "1928fba2a2b644fca3c9e87990ea34ca"

#--- ST.FORM DEF OUTCOME  --- 
with st.spinner("Collecting your data..."): 
    if submitted:
        data = yf.Ticker(stockTicker).info
        analysis = yf.Ticker(stockTicker).financials
        # headlines = yf.Ticker(stockTicker).news
        news_url = f"https://newsapi.org/v2/everything?q={stockTicker}&apiKey={api_key}"
        response = requests.get(news_url)

        tab1, tab2, tab3 = st.tabs(["News", "Summary", "Financials"]) 
        #--- DATA TAB DEF --- 
        with tab2:
            st.subheader("Finance Data Relevant to Selected Stock:")
            st.write(data) 
        #--- NEWS TAB DEF --- 
        with tab1:
            st.subheader("News Lines Relevant to Selected Stock:") 
            if response.status_code == 200:
                news_data = response.json() 
                articles = news_data["articles"]

            for article in articles:
                st.subheader(f"{article['title']}")
                st.write(f"{article['description']}")
                st.caption(f"**Source:** {article['source']['name']}")
                st.caption(f"**Published At:** {article['publishedAt']}")
                st.write(f"**URL:** [{article['url']}]({article['url']})")
                st.write("---")
        with tab3:
            st.subheader("Financials Table:") 
            st.table(analysis)
    #else:
        #st.error("Error fetching news data. Please try again later.")
            