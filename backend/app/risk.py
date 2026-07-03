def calculate_risk(market, news):
    score = 20
    flags = []

    if market.get('volatility_percent', 0) > 4:
        score += 25
        flags.append('High short-term volatility.')
    elif market.get('volatility_percent', 0) > 2:
        score += 10
        flags.append('Moderate volatility.')

    if market.get('volume_ratio', 1) < 0.6:
        score += 10
        flags.append('Volume is below recent average.')

    negative_news = [item for item in news if item.get('sentiment') == 'negative' and item.get('confidence', 0) >= 0.35]
    if negative_news:
        score += min(20, len(negative_news) * 6)
        flags.append('Negative news sentiment detected.')

    if not news:
        score += 8
        flags.append('No recent news found; sentiment confidence is limited.')

    return {'risk_score': max(0, min(100, round(score, 2))), 'risk_flags': flags}
