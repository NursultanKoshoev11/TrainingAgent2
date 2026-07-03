import importlib
import os

REQUIRED_MODULES = [
    'app.server',
    'app.api',
    'app.api_extra',
    'app.api_explain',
    'app.api_screener',
    'app.advice_service',
    'app.market_service',
    'app.news_data',
    'app.screener',
    'app.database',
]

OPTIONAL_MODULES = [
    'ccxt',
    'psycopg',
    'cryptofeed',
]


def module_status(name):
    try:
        importlib.import_module(name)
        return {'name': name, 'available': True}
    except Exception as exc:
        return {'name': name, 'available': False, 'error': str(exc)}


def diagnostics_report():
    required = [module_status(name) for name in REQUIRED_MODULES]
    optional = [module_status(name) for name in OPTIONAL_MODULES]
    env = {
        'database_url_configured': bool(os.getenv('DATABASE_URL')),
        'cryptopanic_configured': bool(os.getenv('CRYPTOPANIC_API_KEY')),
        'sentiment_model_configured': bool(os.getenv('SENTIMENT_MODEL_URL')),
        'gdelt_enabled': os.getenv('GDELT_ENABLED', 'false').lower() == 'true',
        'streaming_enabled': os.getenv('STREAMING_ENABLED', 'false').lower() == 'true',
    }
    required_ok = all(item['available'] for item in required)
    return {
        'required_ok': required_ok,
        'required_modules': required,
        'optional_modules': optional,
        'environment': env,
    }
