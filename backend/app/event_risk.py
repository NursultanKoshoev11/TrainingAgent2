HIGH_RISK_TERMS = {
    'lawsuit', 'ban', 'probe', 'fine', 'sec', 'regulator', 'liquidation',
    'bankruptcy', 'delist', 'halt', 'exploit', 'breach', 'collapse'
}


def detect_event_risk(news):
    flags = []
    score = 0
    for item in news:
        title = item.get('title', '').lower()
        matched = sorted(term for term in HIGH_RISK_TERMS if term in title)
        if matched:
            score += min(20, len(matched) * 5)
            flags.append({'title': item.get('title'), 'terms': matched})
    return {'event_risk_score': min(100, score), 'event_risk_flags': flags}
