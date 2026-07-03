def summarize_trades(trades=None):
    trades = trades or []
    buy_volume = 0
    sell_volume = 0
    for trade in trades:
        side = str(trade.get('side', '')).lower()
        amount = float(trade.get('amount', 0))
        if side == 'buy':
            buy_volume += amount
        elif side == 'sell':
            sell_volume += amount
    total = buy_volume + sell_volume
    flow_balance = 0 if total == 0 else round((buy_volume - sell_volume) / total, 4)
    if flow_balance > 0.2:
        state = 'aggressive_buying'
    elif flow_balance < -0.2:
        state = 'aggressive_selling'
    else:
        state = 'mixed_flow'
    return {'buy_volume': round(buy_volume, 6), 'sell_volume': round(sell_volume, 6), 'flow_balance': flow_balance, 'state': state}
