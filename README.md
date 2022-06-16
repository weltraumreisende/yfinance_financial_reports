# yfinance_financial_reports
Financial reports of Japanese companies from Yahoo Finance using yfinance

This web app uses yfinance and streamlit to display Profit Loss, Balance Sheet Cash Flow of Japanese companies by input 4 digits of the stock codes. The program automatically add ".T" for the stock code to enable yahoo finance search. The financial reports displayed are for past 4 years annual data.

For example if you would like to display Toyota's financial reports for past 4 years, input 7203, then the program adds ".T" to 7203, and searches financial data of stock code "7203.T". 

```python
# The prerequisites 

# To run this web app, you need to install streamlit and yfinance.

# to download streamlit
pip install streamlit 

#to download yfinance
pip install yfinance
```
```python
#to run this app on python
streamlit run financial_reports.py
```
