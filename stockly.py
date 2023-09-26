import yfinance as yf
import streamlit as st
import pandas as pd 
from pandas_datareader import data as pdr
import time as t 

# --- PAGE CONFIG --- 
st.set_page_config(
    page_title="Stockly",
    page_icon="chart_with_upwards_trend",
    layout="centered",
)
yf.pdr_override()
# --- TICKER INFO & DATA --- 
st.subheader("Stock Data AI Aggregator! Relevant Data & News...")

with st.sidebar:
    st.header("Welcome to Stockly!")
    st.subheader("Investing made easy!") 
    st.text("Stockly is a tech startup focused in making financial data easy and accurate! Make informed decisions with faster and more relevant information!")
    st.divider()
    st.caption("Navigate over to our Test Data Engine")

with st.form("Stock Ticker Symbol Selector"):
    stockTicker = st.text_input("Enter the Stock Ticker Symbol here...") 
    submitted = st.form_submit_button("Get Data!") 
if submitted: 
    if not stockTicker:
        st.info("Please provide a valid Stock Ticker Label") 
        st.stop()

with st.spinner("Collecting your data..."): 
    if submitted:
        data = yf.Ticker(stockTicker).info
        headlines = yf.Ticker(stockTicker).news
        tab1, tab2 = st.tabs(["Data", "News"]) 
        with tab1:
            st.subheader("Finance Data Relevant to Selected Stock:")
            st.write(data) 
        with tab2:
            st.subheader("News Lines Relevant to Selected Stock:") 
            st.dataframe(
                headlines,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "link": st.column_config.LinkColumn(
                        "Links",
                    ),
                }
            )
            
