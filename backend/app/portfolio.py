def analyze_watchlist_exposure(advice_items):
    valid = [item for item in advice_items if 'recommendation' in item]
    if not valid:
        return {
            'portfolio_bias': 'unknown',
            'average_final_score': 0,
            'average_risk_score': 0,
            'notes': ['No valid advice items available.'],
        }

    avg_final = round(sum(item.get('final_score', 0) for item in valid) / len(valid), 2)
    avg_risk = round(sum(item.get('risk_score', 0) for item in valid) / len(valid), 2)

    if avg_risk >= 70:
        bias = 'high_risk'
    elif avg_final >= 60:
        bias = 'constructive'
    elif avg_final <= 40:
        bias = 'defensive'
    else:
        bias = 'neutral'

    notes = []
    if avg_risk >= 70:
        notes.append('Average risk is high across the watchlist.')
    if avg_final >= 60 and avg_risk < 70:
        notes.append('Signals are generally constructive, but still advisory-only.')
    if avg_final <= 40:
        notes.append('Signals are generally weak or defensive.')

    return {
        'portfolio_bias': bias,
        'average_final_score': avg_final,
        'average_risk_score': avg_risk,
        'notes': notes,
    }
