from app.advisor_core import score_market
from app.market_data import fetch_candles


def build_market_snapshot(symbol='BTC/USDT', exchange='binance', timeframe='1h'):
    candles = fetch_candles(exchange, symbol, timeframe, limit=120)
    closes = [item['close'] for item in candles]
    volumes = [item['volume'] for item in candles]
    analysis = score_market(closes, volumes)
    return {
        'exchange': exchange,
        'symbol': symbol,
        'timeframe': timeframe,
        'latest_price': closes[-1] if closes else None,
        'candle_count': len(candles),
        **analysis,
    }
