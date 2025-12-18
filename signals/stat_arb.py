import numpy as np
import pandas as pd

def zscore(series, window=60):
    mean = series.rolling(window).mean()
    std = series.rolling(window).std()
    return (series - mean) / std

def stat_arb_signal(prices, asset_a, asset_b):
    spread = np.log(prices[asset_a]) - np.log(prices[asset_b])
    z = zscore(spread).iloc[-1]

    if z > 2:
        return "SHORT_SPREAD"
    elif z < -2:
        return "LONG_SPREAD"
    else:
        return "NO_TRADE"
