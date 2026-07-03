from app.settings import DEFAULT_EXCHANGE, DEFAULT_TIMEFRAME, symbol_list


def get_watchlist():
    return {
        'default_exchange': DEFAULT_EXCHANGE,
        'default_timeframe': DEFAULT_TIMEFRAME,
        'symbols': symbol_list(),
    }
