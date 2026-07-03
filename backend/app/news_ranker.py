SOURCE_WEIGHTS = {
    'CryptoPanic': 1.0,
    'rss': 0.7,
}


def rank_news(items):
    ranked = []
    for item in items:
        source = item.get('source') or 'rss'
        sentiment_confidence = item.get('confidence', 0.3)
        source_weight = SOURCE_WEIGHTS.get(source, 0.6)
        rank_score = round(source_weight * 50 + sentiment_confidence * 50, 2)
        enriched = dict(item)
        enriched['rank_score'] = rank_score
        ranked.append(enriched)
    ranked.sort(key=lambda row: row.get('rank_score', 0), reverse=True)
    return ranked
