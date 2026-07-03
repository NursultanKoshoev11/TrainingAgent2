def estimate_liquidity(market):
    volume_ratio = market.get('volume_ratio', 1)
    volatility = market.get('volatility_percent', 0)
    score = 50
    flags = []

    if volume_ratio >= 1.5:
        score += 20
    elif volume_ratio < 0.6:
        score -= 20
        flags.append('Low relative volume can reduce signal reliability.')

    if volatility > 4:
        score -= 20
        flags.append('High volatility can reduce effective liquidity.')
    elif volatility > 2:
        score -= 10

    score = max(0, min(100, round(score, 2)))
    return {'liquidity_score': score, 'liquidity_flags': flags}
