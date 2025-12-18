import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from data.loader import load_prices, compute_returns
from signals.momentum import momentum_signal
from signals.stat_arb import stat_arb_signal
from portfolio.allocator import allocate_weights
from risk.risk_manager import RiskManager
from execution.paper_broker import PaperBroker
from dashboard.summary import print_summary
from data.universe import nifty_100

TICKERS = nifty_100()


def main():
    prices = load_prices(TICKERS)
    returns = compute_returns(prices)

    # Signals
    mom_signals = momentum_signal(returns)
    pair_signal = stat_arb_signal(prices, "RELIANCE.NS", "ONGC.NS")

    # Portfolio
    weights = allocate_weights(mom_signals)

    # Risk
    risk = RiskManager()
    equity = 1.0
    risk.update_equity(equity)
    risk_ok = risk.check_drawdown(equity)

    # Execution
    broker = PaperBroker()
    if risk_ok:
        for sym, w in weights.items():
            if w != 0:
                side = "BUY" if w > 0 else "SELL"
                broker.execute(sym, side, abs(w))

    # Dashboard
    print_summary(
        regime="TRENDING / LOW VOL",
        momentum_signals=mom_signals,
        pair_signal=pair_signal,
        risk_ok=risk_ok
    )

if __name__ == "__main__":
    main()
