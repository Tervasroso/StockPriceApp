import yfinance as yf
import streamlit as st

st.write("""
         # Nokian vuoden 2022 osakekurssi ja volyymi
         """)

# Määritä ticker symboli (Nokian symboli on NOK) - Define ticker Symbol
# Ticker symboli on uniikki koodi, jolla tunnistetaan pörssiyhtiö. # A ticker is a type of stock symbol that describes information about the stock of a company.
# All stock symbals https://stockanalysis.com/stocks/

tickerSymbol = 'NOK'
# Haetaan tämän symbolin data. - get data for this symbol
tickerData = yf.Ticker(tickerSymbol)
# Haetaan tämän tickerin historiatietoja - get historic data for this Ticker
tickerDf = tickerData.history(period='1d', start='2022-1-1', end='2022-12-31')

st.write("""
        ## Osakekurssi (Closing Price)
         """)
st.line_chart(tickerDf.Close)
st.write("""
        ## Volyymi (Volume)
         """)
st.line_chart(tickerDf.Volume)