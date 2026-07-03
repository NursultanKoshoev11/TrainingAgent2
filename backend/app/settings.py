import os


DEFAULT_EXCHANGE = os.getenv('DEFAULT_EXCHANGE', 'binance')
DEFAULT_SYMBOLS = os.getenv('DEFAULT_SYMBOLS', 'BTC/USDT,ETH/USDT,SOL/USDT')
DEFAULT_TIMEFRAME = os.getenv('DEFAULT_TIMEFRAME', '1h')
DEFAULT_NEWS_LIMIT = int(os.getenv('DEFAULT_NEWS_LIMIT', '12'))


def symbol_list():
    return [item.strip() for item in DEFAULT_SYMBOLS.split(',') if item.strip()]
