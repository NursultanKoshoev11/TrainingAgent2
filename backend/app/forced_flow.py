def neutral_forced_flow_context():
    return {
        'forced_flow_score': 50,
        'forced_flow_flags': ['Forced-flow provider is not connected yet.'],
    }


def score_forced_flow_spike(notional_usd):
    value = float(notional_usd)
    score = 50
    flags = []
    if value > 100000000:
        score -= 25
        flags.append('Large forced-flow spike detected; volatility risk may be high.')
    elif value > 25000000:
        score -= 10
        flags.append('Moderate forced-flow spike detected.')
    return {'forced_flow_score': max(0, min(100, score)), 'forced_flow_flags': flags}
