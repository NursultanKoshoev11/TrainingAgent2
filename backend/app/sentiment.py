POSITIVE_WORDS = {
    'approval', 'approved', 'adoption', 'growth', 'rally', 'surge', 'record',
    'upgrade', 'partnership', 'launch', 'inflow', 'institutional', 'breakthrough'
}

NEGATIVE_WORDS = {
    'lawsuit', 'ban', 'outflow', 'crash', 'probe', 'delay', 'breach',
    'risk', 'collapse', 'liquidation', 'selloff', 'warning', 'fine'
}


def score_text(text):
    words = {word.strip('.,:;!?()[]{}').lower() for word in text.split()}
    positive = len(words & POSITIVE_WORDS)
    negative = len(words & NEGATIVE_WORDS)
    raw = positive - negative
    score = max(0, min(100, 50 + raw * 12.5))
    confidence = min(0.85, 0.25 + (positive + negative) * 0.12)
    if score >= 60:
        label = 'positive'
    elif score <= 40:
        label = 'negative'
    else:
        label = 'neutral'
    return {'label': label, 'score': round(score, 2), 'confidence': round(confidence, 2)}


def enrich_news(items):
    result = []
    for item in items:
        scored = score_text(item.get('title', ''))
        new_item = dict(item)
        new_item['sentiment'] = scored['label']
        new_item['sentiment_score'] = scored['score']
        new_item['confidence'] = scored['confidence']
        result.append(new_item)
    return result


def aggregate(items):
    if not items:
        return 50
    total_weight = sum(item.get('confidence', 0) for item in items)
    if total_weight == 0:
        return 50
    weighted = sum(item.get('sentiment_score', 50) * item.get('confidence', 0) for item in items)
    return round(weighted / total_weight, 2)
