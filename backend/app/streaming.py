import os

STREAM_SYMBOLS = os.getenv('STREAM_SYMBOLS', 'BTC/USDT,ETH/USDT,SOL/USDT')


def stream_symbols():
    return [item.strip() for item in STREAM_SYMBOLS.split(',') if item.strip()]


def streaming_status():
    return {
        'status': 'planned',
        'mode': 'skeleton',
        'symbols': stream_symbols(),
        'planned_sources': ['binance websocket', 'bybit websocket', 'cryptofeed adapter'],
        'planned_metrics': ['trade flow', 'spread', 'orderbook imbalance', 'volume spike', 'liquidity pressure'],
    }


def normalize_stream_event(source, symbol, event_type, payload):
    return {
        'source': source,
        'symbol': symbol,
        'event_type': event_type,
        'payload': payload,
    }
