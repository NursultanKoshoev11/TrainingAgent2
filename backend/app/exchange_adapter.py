import os

from app.market_data import fetch_candles as fetch_public_candles


def use_ccxt():
    return os.getenv('USE_CCXT', 'false').lower() == 'true'


def fetch_ccxt_candles(exchange, symbol, timeframe='1h', limit=120):
    try:
        import ccxt
    except ImportError as exc:
        raise RuntimeError('ccxt is not installed. Install ccxt or set USE_CCXT=false.') from exc

    if not hasattr(ccxt, exchange):
        raise ValueError('unsupported ccxt exchange: ' + exchange)

    exchange_class = getattr(ccxt, exchange)
    client = exchange_class({'enableRateLimit': True})
    rows = client.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    return [
        {
            'timestamp': int(row[0]),
            'open': float(row[1]),
            'high': float(row[2]),
            'low': float(row[3]),
            'close': float(row[4]),
            'volume': float(row[5]),
        }
        for row in rows
    ]


def fetch_candles(exchange, symbol, timeframe='1h', limit=120):
    if use_ccxt():
        return fetch_ccxt_candles(exchange, symbol, timeframe, limit)
    return fetch_public_candles(exchange, symbol, timeframe, limit)
