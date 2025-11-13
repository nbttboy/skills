# 简化估值模型
class Company:
    def __init__(self, revenue_growth, profit_growth, market_cap, profit):
        self.revenue_growth = revenue_growth
        self.profit_growth = profit_growth
        self.market_cap = market_cap
        self.profit = profit

class ValuationModel:
    def calculate_fair_value(self, company):
        # 1. 增长率评估
        growth_rate = company.revenue_growth * 0.4 + \
                      company.profit_growth * 0.6

        # 2. 合理PE区间
        fair_pe_low = growth_rate * 0.8
        fair_pe_high = growth_rate * 1.2

        # 3. 当前估值状态
        current_pe = company.market_cap / company.profit

        if current_pe < fair_pe_low:
            return "低估", "可加大定投"
        elif current_pe > fair_pe_high:
            return "高估", "暂停或减少定投"
        else:
            return "合理", "正常定投"

# 实战案例
# nvidia_2023 = Company(
#     revenue_growth = 0.60,  # 60%增长
#     profit_growth = 0.80,   # 80%增长
#     market_cap = 1000, # Example value
#     profit = 45 # Example value
# )
#
# valuation_model = ValuationModel()
# status, action = valuation_model.calculate_fair_value(nvidia_2023)
# print(f"Valuation Status: {status}, Action: {action}")
