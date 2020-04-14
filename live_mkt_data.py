from ibapi.client import EClient
from ibapi.common import TickerId, TickAttrib
from ibapi.ticktype import TickType, TickTypeEnum
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract, ContractDetails


class DemoApp(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
	
	def error(self, reqId, errorCode, errorString):
		print("Error ", reqId, " ", errorCode, " ", errorString)
	
	def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, attrib: TickAttrib):
		print("Tick Price. Ticker Id:", reqId, "tick type:", TickTypeEnum.to_str(tickType), "Price:", price, end=" ")
	
	def tickSize(self, reqId: TickerId, tickType: TickType, size: int):
		print("Tick Size. Ticker Id:", reqId, "tick type:", TickTypeEnum.to_str(tickType), "Size:", size)


def main():
	app = DemoApp()
	
	app.connect("127.0.0.1", 7496, 0)
	
	# id = app.reqIds(0)
	
	contract = Contract()
	contract.symbol = "AAPL"
	contract.secType = "STK"
	contract.exchange = "SMART"
	contract.currency = "USD"
	# contract.primaryExchange = "ISLAND"
	
	app.reqContractDetails(1, contract)
	app.reqMktData(1, contract, "", False, False, [])
	
	app.run()
	
	print()


# app.disconnect()


if __name__ == '__main__':
	main()
