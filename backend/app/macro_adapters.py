MACRO_ADAPTERS = [
    {'name': 'dollar_index', 'status': 'planned'},
    {'name': 'equity_indices', 'status': 'planned'},
    {'name': 'bond_yields', 'status': 'planned'},
    {'name': 'economic_calendar', 'status': 'planned'},
]


def macro_adapters_status():
    return {
        'status': 'planned',
        'adapters': MACRO_ADAPTERS,
        'note': 'Macro adapters are reserved for future risk context enrichment.',
    }


def normalize_macro_snapshot(source, value, score=50, flags=None):
    return {
        'source': source,
        'value': value,
        'macro_score': score,
        'macro_flags': flags or [],
    }
