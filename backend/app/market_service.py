from app.advisor_core import score_market
from app.exchange_adapter import fetch_candles
from app.memory_cache import cache_get, cache_set


def build_market_snapshot(symbol='BTC/USDT', exchange='binance', timeframe='1h'):
    cache_key = f'market:{exchange}:{symbol}:{timeframe}'
    cached = cache_get(cache_key)
    if cached:
        return cached
    candles = fetch_candles(exchange, symbol, timeframe, limit=120)
    closes = [item['close'] for item in candles]
    volumes = [item['volume'] for item in candles]
    analysis = score_market(closes, volumes)
    snapshot = {
        'exchange': exchange,
        'symbol': symbol,
        'timeframe': timeframe,
        'latest_price': closes[-1] if closes else None,
        'candle_count': len(candles),
        **analysis,
    }
    return cache_set(cache_key, snapshot, ttl_seconds=30)
