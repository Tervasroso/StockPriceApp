import yfinance as yf
import streamlit as st

st.write("""
         # Nokian vuoden 2022 osakekurssi ja volyymi
         """)

# Määritä ticker symboli (Nokian symboli on NOK)
# A ticker is a type of stock symbol that describes information about the stock of a company.

tickerSymbol = 'NOK'
# Haetaan tämän symbolin data.
tickerData = yf.Ticker(tickerSymbol)
# Haetaan tämän tickerin historiatietoja
tickerDf = tickerData.history(period='1d', start='2022-1-1', end='2022-12-31')

st.write("""
        ## Osakekurssi (Closing Price)
         """)
st.line_chart(tickerDf.Close)
st.write("""
        ## Volyymi (Volume)
         """)
st.line_chart(tickerDf.Volume)