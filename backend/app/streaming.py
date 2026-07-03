import json
import os
import time

STREAM_SYMBOLS = os.getenv('STREAM_SYMBOLS', 'BTC/USDT,ETH/USDT,SOL/USDT')


def stream_symbols():
    return [item.strip() for item in STREAM_SYMBOLS.split(',') if item.strip()]


def stream_config():
    return {
        'enabled': os.getenv('STREAMING_ENABLED', 'false').lower() == 'true',
        'provider': os.getenv('STREAMING_PROVIDER', 'snapshot-polling'),
        'poll_interval_seconds': int(os.getenv('STREAM_POLL_INTERVAL_SECONDS', '10')),
        'symbols': stream_symbols(),
    }


def streaming_status():
    return {
        'status': 'planned',
        'mode': 'event-layer-ready',
        'config': stream_config(),
        'planned_sources': ['binance websocket', 'bybit websocket', 'cryptofeed adapter'],
        'planned_metrics': ['trade flow', 'spread', 'orderbook imbalance', 'volume spike', 'liquidity pressure'],
    }


def normalize_stream_event(source, symbol, event_type, payload):
    return {
        'source': source,
        'symbol': symbol,
        'event_type': event_type,
        'payload': payload,
        'created_at_ms': int(time.time() * 1000),
    }


def write_event_line(path, event):
    with open(path, 'a', encoding='utf-8') as handle:
        handle.write(json.dumps(event) + '\n')
