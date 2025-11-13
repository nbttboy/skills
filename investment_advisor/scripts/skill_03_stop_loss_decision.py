# 止损决策模型
class StopLossDecision:
    def __init__(self, entry_price, current_price, market_trend, my_view=None, fundamentals_healthy=True):
        self.entry_price = entry_price
        self.current_price = current_price
        self.market_trend = market_trend
        self.my_view = my_view
        self.fundamentals_healthy = fundamentals_healthy
        self.loss_percent = (current_price - entry_price) / entry_price

    def should_stop_loss(self):
        # 规则1: 亏损超过阈值
        if self.loss_percent < -0.15:  # -15%
            return True, "亏损超过15%止损线"

        # 规则2: 判断与市场冲突
        if self.market_trend == "下跌" and self.my_view == "看多":
            return True, "判断错误，市场走势与预期相反"

        # 规则3: 基本面恶化
        if not self.fundamentals_healthy:
            return True, "基本面发生实质性恶化"

        return False, "持有"
