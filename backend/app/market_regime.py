def classify_market_regime(market):
    score = market.get('score', 50)
    volatility = market.get('volatility_percent', 0)

    if volatility >= 4:
        volatility_label = 'high_volatility'
    elif volatility >= 2:
        volatility_label = 'moderate_volatility'
    else:
        volatility_label = 'normal_volatility'

    if score >= 65:
        direction = 'constructive'
    elif score <= 35:
        direction = 'defensive'
    else:
        direction = 'neutral'

    return {
        'direction': direction,
        'volatility': volatility_label,
        'regime': direction + '_' + volatility_label,
    }
