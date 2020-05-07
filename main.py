import os

import pandas as pd

from ibapi.utils import iswrapper
from ibapi.client import EClient
from ibapi.common import TickerId, TickAttrib, BarData
from ibapi.ticktype import TickType, TickTypeEnum
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract, ContractDetails

COLUMNS = ["date", "open", "high", "low", "close", "volume", "trades", "average"]


# x = pd.DataFrame(columns=["date", "close"])
#
# x = x.append({"date": "test1", "close": "test2"}, ignore_index=True)


class DemoApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.hist_data = pd.DataFrame(columns=COLUMNS)
    
    def error(self, reqId, errorCode, errorString):
        print("Error ", reqId, " ", errorCode, " ", errorString)
    
    def historicalData(self, reqId: int, bar: BarData):
        self.hist_data = self.hist_data.append(
            pd.DataFrame({"date": [bar.date], "open": [bar.open], "high": [bar.high], "low": [bar.low],
                          "close": [bar.close], "volume": [bar.volume], "trades": [bar.barCount],
                          "average": [bar.average]}),
            ignore_index=True
        )
    
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        self.hist_data.to_csv("C:\\Users\\hrist\\Programming\\IB_API_demo\\c_hist_data.csv")
        print()
    
    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.next_val_id = orderId
        print("Next valid id: {}".format(orderId))
    
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        super().contractDetails(reqId, contractDetails)
        self.contract_details = contractDetails
    
    def contractDetailsEnd(self, reqId: int):
        super().contractDetailsEnd(reqId)
        print()
    
    def fundamentalData(self, reqId: TickerId, data: str):
        super().fundamentalData(reqId, data)
        self.fund_data = data
        print(type(data))
        print(data)
        x = 5
    
    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, attrib: TickAttrib):
        print("Tick Price. Ticker Id:", reqId, "tick type:", TickTypeEnum.to_str(tickType), "Price:", price, end=" ")
    
    def tickSize(self, reqId: TickerId, tickType: TickType, size: int):
        print("Tick Size. Ticker Id:", reqId, "tick type:", TickTypeEnum.to_str(tickType), "Size:", size)

    def tickString(self, reqId: TickerId, tickType: TickType, value: str):
        super().tickString(reqId, tickType, value)


def main():
    app = DemoApp()
    
    app.connect("127.0.0.1", 4001, 0)  # 7496 4001
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
    # id = app.reqIds(0)
    
    contract1 = Contract()
    contract1.symbol = "OXLC"
    contract1.secType = "STK"
    contract1.exchange = "SMART"
    contract1.currency = "USD"
    
    contract2 = Contract()
    contract2.symbol = "FRC PRG"
    contract2.secType = "STK"
    contract2.exchange = "SMART"
    contract2.currency = "USD"
    
    # app.reqHistoricalData(1, contract1, endDateTime="", durationStr="1 Y", barSizeSetting="1 day",
    #                       whatToShow="TRADES", useRTH=1, formatDate=1, keepUpToDate=False, chartOptions=[]) # TRADES ADJUSTED_LAST
    # app.reqHistoricalData(2, contract2, "", "5 W", "1 day", "TRADES", 0, 1, False, [])
    # app.reqContractDetails(1, contract1)
    # app.reqContractDetails(2, contract2)
    
    # ReportsFinSummary
    # ReportsOwnership
    # ReportSnapshot
    # ReportsFinStatements
    # RESC
    # CalendarReport
    # app.reqFundamentalData(11, contract1, "ReportsFinSummary", [])
    
    # genericTickList:
    #   - Fundamental Ratios - 258
    #   - IB Dividends - 456
    app.reqMktData(1, contract1, "258, 456", False, False, [])
    
    app.run()


if __name__ == '__main__':
    main()

# x = pd.DataFrame([1, 1, 1, 1, 1, 1, 1], columns=COLUMNS)
#
# x = pd.DataFrame(columns=COLUMNS)
# y = pd.DataFrame({"date": [1], "open": [2], "high": [3], "low": [4], "close": [5], "volume": [10], "trades": [4]})
# x = x.append(y, ignore_index=True)
#
# x.to_csv("")
