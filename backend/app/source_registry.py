MARKET_SOURCES = [
    {'name': 'binance', 'type': 'public_candles', 'enabled': True},
    {'name': 'bybit', 'type': 'public_candles', 'enabled': True},
]

NEWS_SOURCES = [
    {'name': 'cointelegraph_rss', 'type': 'rss', 'enabled': True},
    {'name': 'coindesk_rss', 'type': 'rss', 'enabled': True},
]

ANALYSIS_MODULES = [
    {'name': 'market_score', 'enabled': True},
    {'name': 'news_sentiment', 'enabled': True},
    {'name': 'risk_score', 'enabled': True},
    {'name': 'final_advice', 'enabled': True},
]


def registry():
    return {
        'market_sources': MARKET_SOURCES,
        'news_sources': NEWS_SOURCES,
        'analysis_modules': ANALYSIS_MODULES,
    }
