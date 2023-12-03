# pip install ib_insync
from IPython.core.display import display
from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7496, readonly=True)

# positions = ib.positions()
#
# matches = ib.reqMatchingSymbols('intc')

# contract = Stock('BAC PRP', 'SMART', 'USD')
# contract = Bond(secIdType='CUSIP', secId='94974BGQ7')
contract = Bond(symbol='94974BGQ7', exchange='SMART', currency='USD')

contract_details = ib.reqContractDetails(contract)[0]
available_data_from = ib.reqHeadTimeStamp(contract, whatToShow='TRADES',
                                          useRTH=True)  # the earliest date of available bar data

bars = ib.reqHistoricalData(
    contract,
    endDateTime='',
    durationStr='10 Y',
    barSizeSetting='1 day',
    whatToShow='TRADES',
    useRTH=True,
    formatDate=1)

# 456 - dividends
# 258 - fundamental ratios
ticker = ib.reqMktData(contract, '456, 258')

df = util.df(bars)
display(df.head())
util.barplot(bars[-100:], title=contract.symbol)

# ib.reqMarketDataType(4) # delayed data
spx = Index('SPX', 'CBOE')
contracts = ib.qualifyContracts(spx)  # fills empty attributes in input contracts
# tickers = ib.reqTickers(spx)

chains = ib.reqSecDefOptParams(spx.symbol, '', spx.secType, spx.conId)
util.df(chains)

ib.disconnect()
