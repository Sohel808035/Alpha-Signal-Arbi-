def print_summary(regime, momentum_signals, pair_signal, risk_ok):
    print("\n==============================")
    print("ALPHA TERMINAL – DAILY DECISION")
    print("==============================")
    print(f"Market Regime : {regime}")
    print(f"Risk Status   : {'ENABLED' if risk_ok else 'HALTED'}")

    print("\nMomentum Trades:")
    for k, v in momentum_signals.items():
        side = "BUY" if v > 0 else "SELL"
        print(f"  {side} {k}")

    print("\nStat-Arb Pair:")
    print(f"  RELIANCE / ONGC : {pair_signal}")
    print("==============================\n")
