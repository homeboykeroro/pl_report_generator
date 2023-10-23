from decimal import Decimal
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from market_mover_monitor.src.ibapi.utils import decimalMaxString, floatMaxString
from utils.log_util import get_logger

logger = get_logger(console_log=False)

class IBConnector(EWrapper, EClient):
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, self)

def pnlSingle(self, reqId: int, pos: Decimal, dailyPnL: float,
              unrealizedPnL: float, realizedPnL: float, value: float):
    super(self).pnlSingle(reqId, pos, dailyPnL,
                          unrealizedPnL, realizedPnL, value)
    print("Daily PnL Single. ReqId:", reqId, "Position:", decimalMaxString(pos),
          "DailyPnL:", floatMaxString(
              dailyPnL), "UnrealizedPnL:", floatMaxString(unrealizedPnL),
          "RealizedPnL:", floatMaxString(realizedPnL), "Value:", floatMaxString(value))

def position(self, account: str, contract: Contract, position: Decimal, avgCost: float):
    super(self).position(account, contract, position, avgCost)
    print("Position.", "Account:", account, "Symbol:", contract.symbol, "SecType:",
          contract.secType, "Currency:", contract.currency,
          "Position:", decimalMaxString(position), "Avg cost:", floatMaxString(avgCost))
