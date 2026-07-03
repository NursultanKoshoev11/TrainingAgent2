SOCIAL_ADAPTERS = [
    {'name': 'reddit', 'status': 'planned'},
    {'name': 'x_twitter', 'status': 'planned'},
    {'name': 'telegram_public_channels', 'status': 'planned'},
]


def social_adapters_status():
    return {
        'status': 'planned',
        'adapters': SOCIAL_ADAPTERS,
        'note': 'Social adapters are disabled until API access and source rules are reviewed.',
    }


def normalize_social_signal(source, symbol, text, score=50, confidence=0.3):
    return {
        'source': source,
        'symbol': symbol,
        'text': text,
        'social_score': score,
        'confidence': confidence,
    }
