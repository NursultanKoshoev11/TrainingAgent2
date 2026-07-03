ASSET_PROFILES = {
    'BTC': {'name': 'Bitcoin', 'category': 'store_of_value', 'risk_tier': 'large_cap'},
    'ETH': {'name': 'Ethereum', 'category': 'smart_contracts', 'risk_tier': 'large_cap'},
    'SOL': {'name': 'Solana', 'category': 'smart_contracts', 'risk_tier': 'large_cap'},
    'BNB': {'name': 'BNB', 'category': 'exchange_ecosystem', 'risk_tier': 'large_cap'},
    'XRP': {'name': 'XRP', 'category': 'payments', 'risk_tier': 'large_cap'},
}


def asset_key(symbol):
    return symbol.upper().replace('/', '').replace('USDT', '')


def get_asset_profile(symbol):
    key = asset_key(symbol)
    return ASSET_PROFILES.get(key, {'name': key, 'category': 'unknown', 'risk_tier': 'unknown'})
