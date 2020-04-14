import pandas as pd

from ibapi.client import EClient
from ibapi.common import TickerId, TickAttrib, BarData
from ibapi.ticktype import TickType, TickTypeEnum
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract, ContractDetails

# x = pd.DataFrame(columns=["date", "close"])
#
# x = x.append({"date": "test1", "close": "test2"}, ignore_index=True)


class DemoApp(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
		self.hist_data = pd.DataFrame(columns=["date", "close"])
	
	def error(self, reqId, errorCode, errorString):
		print("Error ", reqId, " ", errorCode, " ", errorString)
	
	def historicalData(self, reqId: int, bar: BarData):
		# self.hist_data.append({"date": bar.date, "close": bar.close}, ignore_index=True)
		print(bar)


def main():
	app = DemoApp()
	
	app.connect("127.0.0.1", 7496, 0)
	
	# id = app.reqIds(0)
	
	contract = Contract()
	contract.symbol = "AAPL"
	contract.secType = "STK"
	contract.exchange = "SMART"
	contract.currency = "USD"
	
	app.reqHistoricalData(1, contract, "", "1 D", "1 min", "TRADES", 0, 1, False, [])
	
	app.run()


# print()


# app.disconnect()


if __name__ == '__main__':
	main()
