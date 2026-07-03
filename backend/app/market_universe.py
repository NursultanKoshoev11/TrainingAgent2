DEFAULT_UNIVERSE = [
    'BTC/USDT',
    'ETH/USDT',
    'SOL/USDT',
    'BNB/USDT',
    'XRP/USDT',
    'ADA/USDT',
    'DOGE/USDT',
    'AVAX/USDT',
    'LINK/USDT',
    'TON/USDT',
]


def market_universe(limit=None):
    if limit is None:
        return DEFAULT_UNIVERSE
    return DEFAULT_UNIVERSE[:limit]
