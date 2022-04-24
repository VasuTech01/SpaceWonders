import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price

**Shown** are the closing price and volume of Google!
> vasu saini

| Name | Description |
| ----------- | ----------- |
| **Vasu** | **Don** |
| Paragraph | Text |
""")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.write(df)
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end="2020-5-31")
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
