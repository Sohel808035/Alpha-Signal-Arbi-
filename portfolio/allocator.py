import pandas as pd

def allocate_weights(signal_dict):
    n = len(signal_dict)
    if n == 0:
        return pd.Series(dtype=float)

    w = 1.0 / n
    return pd.Series({k: v * w for k, v in signal_dict.items()})
