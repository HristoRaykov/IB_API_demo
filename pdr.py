import os
import pandas as pd
import pandas_datareader as pdr


# query = 'WIKI/AAPL'
# data = pdr.DataReader('^DJI', 'stooq')

# # Meta Data
# https://api.tiingo.com/tiingo/daily/<ticker>
#
# # Latest Price
# https://api.tiingo.com/tiingo/daily/<ticker>/prices
#
# # Historical Prices
# https://api.tiingo.com/tiingo/daily/<ticker>/prices?startDate=2012-1-1&endDate=2016-1-1


TIINGO_API_KEY = os.getenv("TIINGO_API_KEY")
# https://api.tiingo.com/tiingo/daily/ETY/prices?token=5bbb9e7c4c5aab5c84531c9b8bc04c3b56848e21
data = pdr.get_data_tiingo("PDI", api_key=TIINGO_API_KEY)
x = data[data["divCash"] != 0]

# tiingo_tickers = pd.read_csv("https://apimedia.tiingo.com/docs/tiingo/daily/supported_tickers.zip")
#
#
#
# data = pdr.get_data_yahoo("ETY", get_actions=True)  # adjust_price=True
#
#
# data = pdr.data.DataReader("ETY", "iex")
