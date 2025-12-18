def momentum_signal(returns, lookback=126, top_n=5):
    scores = returns.rolling(lookback).sum().iloc[-1].dropna()
    ranked = scores.sort_values()

    signals = {}
    for s in ranked.head(top_n).index:
        signals[s] = -1
    for s in ranked.tail(top_n).index:
        signals[s] = 1

    return signals
