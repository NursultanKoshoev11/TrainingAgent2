from app.market_filters import high_risk, low_confidence, top_by_score
from app.universe_service import analyze_universe


def screen_market(exchange='binance', timeframe='1h', limit=10):
    overview = analyze_universe(exchange=exchange, timeframe=timeframe, limit=limit)
    items = overview.get('items', [])
    return {
        'exchange': exchange,
        'timeframe': timeframe,
        'top_setups': top_by_score(items, limit=5),
        'high_risk': high_risk(items),
        'low_confidence': low_confidence(items),
        'raw': overview,
    }
