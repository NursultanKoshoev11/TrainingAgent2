def filter_valid_advice(items):
    return [item for item in items if 'recommendation' in item]


def top_by_score(items, limit=5):
    valid = filter_valid_advice(items)
    valid.sort(key=lambda row: row.get('final_score', -1), reverse=True)
    return valid[:limit]


def high_risk(items, threshold=70):
    valid = filter_valid_advice(items)
    return [item for item in valid if item.get('risk_score', 0) >= threshold]


def low_confidence(items, threshold=30):
    valid = filter_valid_advice(items)
    return [item for item in valid if item.get('confidence', 0) < threshold]
