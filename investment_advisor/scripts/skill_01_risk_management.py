# 伪代码示例
def risk_management(market_volatility, position_profit):
    HIGH_THRESHOLD = 0.2  # Example value
    MEDIUM_THRESHOLD = 0.1 # Example value
    if market_volatility > HIGH_THRESHOLD:
        action = "及时止盈"
        note = "不追高，容易被挂东南枝"
    elif market_volatility > MEDIUM_THRESHOLD:
        action = "减少杠杆"
        note = "震荡期做波段套利"
    else:
        action = "可考虑加杠杆"
        note = "确定性强时放大收益"
    return action, note
