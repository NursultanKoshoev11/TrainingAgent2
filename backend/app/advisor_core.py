from statistics import mean, pstdev


def percent_change(first, last):
    if first == 0:
        return 0
    return round(((last - first) / first) * 100, 2)


def moving_average(values, period):
    if not values:
        return 0
    return round(mean(values[-period:]), 6) if len(values) >= period else round(mean(values), 6)


def volatility(values):
    if len(values) < 3:
        return 0
    changes = []
    for previous, current in zip(values[:-1], values[1:]):
        if previous:
            changes.append((current - previous) / previous)
    return round(pstdev(changes) * 100, 3) if len(changes) > 1 else 0


def score_market(closes, volumes):
    if len(closes) < 20:
        return {"score": 50, "notes": ["Not enough price history."]}
    fast = moving_average(closes, 12)
    slow = moving_average(closes, 26)
    change = percent_change(closes[0], closes[-1])
    vol = volatility(closes[-48:])
    avg_volume = mean(volumes[-20:]) if len(volumes) >= 20 else mean(volumes)
    volume_ratio = round(volumes[-1] / avg_volume, 3) if avg_volume else 1
    score = 50
    notes = []
    if fast > slow:
        score += 12
        notes.append("Short moving average is above long moving average.")
    else:
        score -= 12
        notes.append("Short moving average is below long moving average.")
    if change > 2:
        score += 8
        notes.append("Recent price movement is positive.")
    elif change < -2:
        score -= 8
        notes.append("Recent price movement is negative.")
    if volume_ratio > 1.5:
        score += 5
        notes.append("Volume is above recent average.")
    elif volume_ratio < 0.6:
        score -= 5
        notes.append("Volume is below recent average.")
    if vol > 4:
        score -= 12
        notes.append("Volatility is high.")
    return {
        "score": max(0, min(100, round(score, 2))),
        "change_percent": change,
        "fast_average": fast,
        "slow_average": slow,
        "volatility_percent": vol,
        "volume_ratio": volume_ratio,
        "notes": notes,
    }


def final_advice(market_score, sentiment_score, risk_score):
    final = round((market_score * 0.5) + (sentiment_score * 0.3) - (risk_score * 0.2) + 20, 2)
    final = max(0, min(100, final))
    if risk_score >= 70:
        label = "HIGH_RISK_AVOID"
    elif final >= 72:
        label = "STRONG_POSITIVE_SETUP"
    elif final >= 58:
        label = "POSITIVE_SETUP"
    elif final <= 35:
        label = "NEGATIVE_SETUP"
    else:
        label = "WAIT"
    return {"label": label, "final_score": final}
