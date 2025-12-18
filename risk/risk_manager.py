class RiskManager:
    def __init__(self, max_drawdown=0.15, max_position=0.05):
        self.max_drawdown = max_drawdown
        self.max_position = max_position
        self.peak_equity = 1.0

    def update_equity(self, equity):
        self.peak_equity = max(self.peak_equity, equity)

    def check_drawdown(self, equity):
        dd = (self.peak_equity - equity) / self.peak_equity
        return dd < self.max_drawdown

    def clip_weight(self, w):
        return max(min(w, self.max_position), -self.max_position)
