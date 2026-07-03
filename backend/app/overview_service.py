from app.advice_service import build_advice
from app.settings import DEFAULT_EXCHANGE, DEFAULT_TIMEFRAME, symbol_list


def build_overview(exchange=DEFAULT_EXCHANGE, timeframe=DEFAULT_TIMEFRAME):
    items = []
    for symbol in symbol_list():
        try:
            items.append(build_advice(symbol=symbol, exchange=exchange, timeframe=timeframe))
        except Exception as exc:
            items.append({'symbol': symbol, 'service_error': str(exc)})
    items.sort(key=lambda item: item.get('final_score', -1), reverse=True)
    return {'exchange': exchange, 'timeframe': timeframe, 'count': len(items), 'items': items}
