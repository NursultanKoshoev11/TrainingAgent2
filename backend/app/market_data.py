import json
import urllib.parse
import urllib.request


def normalize_pair(symbol):
    text = symbol.upper().replace('/', '').strip()
    if text.endswith('USDT'):
        return text
    return text + 'USDT'


def _read_json(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'TrainingAgent2/0.1'})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode('utf-8'))


def fetch_binance_candles(symbol, timeframe='1h', limit=120):
    query = urllib.parse.urlencode({'symbol': normalize_pair(symbol), 'interval': timeframe, 'limit': limit})
    rows = _read_json('https://api.binance.com/api/v3/klines?' + query)
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


def _bybit_interval(timeframe):
    mapping = {'1m': '1', '5m': '5', '15m': '15', '30m': '30', '1h': '60', '4h': '240', '1d': 'D'}
    return mapping.get(timeframe, '60')


def fetch_bybit_candles(symbol, timeframe='1h', limit=120):
    query = urllib.parse.urlencode({'category': 'spot', 'symbol': normalize_pair(symbol), 'interval': _bybit_interval(timeframe), 'limit': limit})
    payload = _read_json('https://api.bybit.com/v5/market/kline?' + query)
    rows = list(reversed(payload.get('result', {}).get('list', [])))
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
    name = exchange.lower().strip()
    if name == 'binance':
        return fetch_binance_candles(symbol, timeframe, limit)
    if name == 'bybit':
        return fetch_bybit_candles(symbol, timeframe, limit)
    raise ValueError('supported exchanges: binance, bybit')
