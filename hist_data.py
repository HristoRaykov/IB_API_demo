import pandas as pd

from ibapi.utils import iswrapper
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
		self.hist_data = []
	
	def error(self, reqId, errorCode, errorString):
		print("Error ", reqId, " ", errorCode, " ", errorString)
	
	def historicalData(self, reqId: int, bar: BarData):
		self.hist_data.append(bar)
		print(bar)
	
	def nextValidId(self, orderId: int):
		super().nextValidId(orderId)
		self.next_val_id = orderId
		print("Next valid id: {}".format(orderId))
	
	def contractDetails(self, reqId: int, contractDetails: ContractDetails):
		super().contractDetails(reqId, contractDetails)
		self.contract_details = contractDetails
		print(contractDetails)
	
	def contractDetailsEnd(self, reqId: int):
		super().contractDetailsEnd(reqId)
		print("contract details recieved")


def main():
	app = DemoApp()
	
	app.connect("127.0.0.1", 7496, 0)
	print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
	
	# id = app.reqIds(0)
	
	contract = Contract()
	contract.symbol = "C PRK"
	contract.secType = "STK"
	contract.exchange = "SMART"
	contract.currency = "USD"
	
	app.reqHistoricalData(1, contract, "", "1 W", "1 day", "TRADES", 0, 1, False, [])
	app.reqContractDetails(1, contract)
	
	app.run()
	# print(app.next_val_id)
	#
	# print()
	
	app.disconnect()
	print()


if __name__ == '__main__':
	main()
