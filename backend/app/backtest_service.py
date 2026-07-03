from app.backtest_report import build_backtest_report
from app.exchange_adapter import fetch_candles


def backtest_symbol(symbol='BTC/USDT', exchange='binance', timeframe='1h', limit=200, window=40):
    candles = fetch_candles(exchange=exchange, symbol=symbol, timeframe=timeframe, limit=limit)
    report = build_backtest_report(candles=candles, window=window)
    return {
        'exchange': exchange,
        'symbol': symbol,
        'timeframe': timeframe,
        'limit': limit,
        'window': window,
        'report': report,
        'disclaimer': 'Backtesting is historical research only and does not predict future performance.',
    }
