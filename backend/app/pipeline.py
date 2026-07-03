from app.advice_service import build_advice
from app.db import insert_market_snapshot, insert_news_items
from app.storage import save_signal


def run_symbol_pipeline(symbol='BTC/USDT', exchange='binance', timeframe='1h', save=True):
    advice = build_advice(symbol=symbol, exchange=exchange, timeframe=timeframe)
    result = {'symbol': symbol, 'advice': advice}
    if save:
        result['saved_signal_id'] = save_signal(advice)
        result['saved_market_snapshot_id'] = insert_market_snapshot(advice.get('market', {}))
        result['saved_news_item_ids'] = insert_news_items(symbol, advice.get('news', []))
    return result
