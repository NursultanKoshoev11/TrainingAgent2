MACRO_FACTORS = [
    'interest_rates',
    'dollar_index',
    'equity_market_risk',
    'inflation_expectations',
    'regulatory_headlines',
]


def macro_status():
    return {
        'status': 'planned',
        'factors': MACRO_FACTORS,
        'note': 'Macro data is not connected yet. This module reserves the contract for future data providers.',
    }


def neutral_macro_context():
    return {
        'macro_score': 50,
        'macro_flags': ['Macro context provider is not connected yet.'],
    }
