STREAM_SOURCES = [
    {'name': 'binance_ws', 'status': 'planned'},
    {'name': 'bybit_ws', 'status': 'planned'},
]


def stream_status():
    return {
        'status': 'planned',
        'reason': 'The current MVP uses public candle snapshots. WebSocket streaming is the next service layer.',
        'sources': STREAM_SOURCES,
    }
