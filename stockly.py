import streamlit as st
import pandas as pd 
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from pandas_datareader import data as pdr

#--- CONVERT YFINANCE DATA TO PANDAS --- 
yf.pdr_override() 

#--- STOCK DATA & TICKERS --- 
#tickers = ("APPL, MSFT, GOOG, NVDA") 

#--- STREAMLIT FRAMEWORK --- 
st.title("Welcome to stock.ly")
st.caption("select a stock ticker to analyze:") 

    #--- STOCK SELECTION FORM --- 
with st.form("stock_selector"):
    STOCK_TICKER = st.text_input("Enter the Stock Ticker Symbol here...")
    LENGTH_TIME = st.selectbox(
        label= "Length of time", 
        label_visibility="visible",
        options= ('1m', '1h'),
    ) 
    INTERVAL= '5m'
    submitted = st.form_submit_button("Get Stock Data!") 

if submitted:
    if not STOCK_TICKER:
        st.info("Please provide a valid Stock Ticker Label") 
        st.stop()
    elif not LENGTH_TIME:
        st.info("Please select a valid length of time") 
        st.stop() 
    elif not INTERVAL:
        st.info("Problem with interval") 
        st.stop() 

    #--- STOCK DATA DISPLAY --- 
with st.spinner("Collecting your data..."):
    if submitted:
        data = pdr.get_data_yahoo(STOCK_TICKER, LENGTH_TIME, INTERVAL)
        df = pd.DataFrame(data)
        st.table(df)