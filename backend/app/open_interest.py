def neutral_open_interest_context():
    return {
        'open_interest_score': 50,
        'open_interest_flags': ['Open-interest provider is not connected yet.'],
    }


def score_open_interest_change(change_percent):
    value = float(change_percent)
    score = 50
    flags = []
    if value > 15:
        score -= 15
        flags.append('Open interest increased quickly; leverage risk may be higher.')
    elif value < -15:
        score -= 5
        flags.append('Open interest dropped quickly; market may be deleveraging.')
    return {'open_interest_score': max(0, min(100, score)), 'open_interest_flags': flags}
