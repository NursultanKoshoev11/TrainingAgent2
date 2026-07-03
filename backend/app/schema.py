SCHEMA = {
    'market_snapshots': [
        'id', 'exchange', 'symbol', 'timeframe', 'latest_price', 'market_score',
        'volatility_percent', 'volume_ratio', 'created_at'
    ],
    'news_items': [
        'id', 'source', 'title', 'url', 'published_at', 'related_assets', 'created_at'
    ],
    'sentiment_scores': [
        'id', 'news_item_id', 'label', 'score', 'confidence', 'engine', 'created_at'
    ],
    'advisory_signals': [
        'id', 'symbol', 'recommendation', 'final_score', 'market_score',
        'sentiment_score', 'risk_score', 'quality_flags', 'created_at'
    ],
    'risk_flags': [
        'id', 'advisory_signal_id', 'flag', 'created_at'
    ],
    'backtest_reports': [
        'id', 'symbol', 'timeframe', 'window', 'summary', 'created_at'
    ]
}


def planned_schema():
    return SCHEMA
