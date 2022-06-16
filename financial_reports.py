import pandas as pd
import yfinance as yf
import streamlit as st

st.title("日本企業の財務情報アプリ")
st.sidebar.write("""
### 表示させたい日本企業の
### 4桁の証券コードを入力してください。
### （Tはつけない）
""")

st.sidebar.write("""
##証券コードを入力
""")
code=st.sidebar.text_input('証券コード')
stock_code=code + ".T"

ticker_info = yf.Ticker(stock_code)
st.write(ticker_info.info['longName'])
st.write(stock_code)

option = st.selectbox(
    "表示させる財務諸表データ",("PL","BS","CF")
    )
st.write("PL:損益計算 BS:バランスシート CF:キャッシュフロー")
st.write(option)

if option == "PL":
    ticker_info.financials

if option == "BS":
     ticker_info.balance_sheet

if option == "CF":
      ticker_info.cashflow


    
