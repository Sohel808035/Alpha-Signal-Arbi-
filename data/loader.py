import yfinance as yf
import pandas as pd
import numpy as np

def load_prices(tickers, start="2019-01-01"):
    data = yf.download(
        tickers,
        start=start,
        progress=False,
        auto_adjust=True  # IMPORTANT: prices already adjusted
    )

    # Case 1: Multiple tickers → MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        if "Close" in data.columns.get_level_values(0):
            prices = data["Close"]
        else:
            raise ValueError("Close price not found in Yahoo data")

    # Case 2: Single ticker
    else:
        if "Close" in data.columns:
            prices = data["Close"].to_frame(name=tickers[0])
        else:
            raise ValueError("Close price not found in Yahoo data")

    prices = prices.dropna(how="all")
    prices.columns = [str(c) for c in prices.columns]
    return prices


def compute_returns(prices):
    return np.log(prices).diff().dropna()
