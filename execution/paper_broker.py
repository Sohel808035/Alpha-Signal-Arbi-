class PaperBroker:
    def execute(self, symbol, side, weight):
        print(f"EXECUTE | {side} | {symbol} | weight={round(weight,3)}")
