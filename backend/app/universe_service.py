from app.advice_service import build_advice
from app.market_universe import market_universe


def analyze_universe(exchange='binance', timeframe='1h', limit=10):
    items = []
    for symbol in market_universe(limit=limit):
        try:
            items.append(build_advice(symbol=symbol, exchange=exchange, timeframe=timeframe))
        except Exception as exc:
            items.append({'symbol': symbol, 'service_error': str(exc)})
    items.sort(key=lambda item: item.get('final_score', -1), reverse=True)
    return {'exchange': exchange, 'timeframe': timeframe, 'count': len(items), 'items': items}
