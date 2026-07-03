def neutral_funding_context():
    return {
        'funding_score': 50,
        'funding_flags': ['Funding provider is not connected yet.'],
    }


def score_funding_rate(rate):
    value = float(rate)
    score = 50
    flags = []
    if value > 0.0005:
        score -= 15
        flags.append('Funding is elevated; long-side crowding risk may be higher.')
    elif value < -0.0005:
        score -= 10
        flags.append('Negative funding is elevated; short-side crowding risk may be higher.')
    return {'funding_score': max(0, min(100, score)), 'funding_flags': flags}
