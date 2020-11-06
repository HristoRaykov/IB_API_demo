from tiingo import TiingoClient

client = TiingoClient()

ticker_metadata = client.get_ticker_metadata("GOOGL")

ticker_price = client.get_ticker_price("GOOGL", frequency="weekly")

# Get historical GOOGL prices from August 2017 as JSON, sampled daily
historical_prices = client.get_ticker_price("GOOGL",
                                            fmt='json',
                                            startDate='2017-08-01',
                                            endDate='2017-08-31',
                                            frequency='daily')

tickers = client.list_stock_tickers()

# Get news articles about given tickers or search terms from given domains
articles = client.get_news(tickers=['GOOGL', 'AAPL'],
                           tags=['Laptops'],
                           sources=['washingtonpost.com'],
                           startDate='2017-01-01',
                           endDate='2017-08-31')
