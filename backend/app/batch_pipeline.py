from app.market_universe import market_universe
from app.pipeline import run_symbol_pipeline


def run_batch_pipeline(exchange='binance', timeframe='1h', limit=10, save=True):
    rows = []
    for symbol in market_universe(limit=limit):
        try:
            rows.append(run_symbol_pipeline(symbol=symbol, exchange=exchange, timeframe=timeframe, save=save))
        except Exception as exc:
            rows.append({'symbol': symbol, 'error': str(exc)})
    return {'exchange': exchange, 'timeframe': timeframe, 'count': len(rows), 'items': rows}
