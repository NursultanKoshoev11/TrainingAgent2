def summarize_book(bids=None, asks=None):
    bids = bids or []
    asks = asks or []
    bid_total = sum(float(row[1]) for row in bids if len(row) >= 2)
    ask_total = sum(float(row[1]) for row in asks if len(row) >= 2)
    total = bid_total + ask_total
    balance = 0 if total == 0 else round((bid_total - ask_total) / total, 4)
    if balance > 0.2:
        state = 'buyer_heavy'
    elif balance < -0.2:
        state = 'seller_heavy'
    else:
        state = 'balanced'
    return {'bid_total': round(bid_total, 6), 'ask_total': round(ask_total, 6), 'balance': balance, 'state': state}
