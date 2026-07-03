def build_snapshot(symbol: str, source: str, timeframe: str) -> dict:
    return {
        'symbol': symbol,
        'source': source,
        'timeframe': timeframe,
        'note': 'placeholder snapshot'
    }
