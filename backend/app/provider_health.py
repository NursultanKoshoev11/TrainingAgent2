from app.database import database_status
from app.external_news import cryptopanic_enabled
from app.exchange_adapter import use_ccxt
from app.macro import macro_status
from app.social import social_status
from app.streaming import streaming_status


def provider_health():
    return {
        'database': database_status(),
        'exchange': {
            'mode': 'ccxt' if use_ccxt() else 'public_http',
            'public_sources': ['binance', 'bybit'],
        },
        'news': {
            'cryptopanic_enabled': cryptopanic_enabled(),
            'rss_enabled': True,
        },
        'streaming': streaming_status(),
        'macro': macro_status(),
        'social': social_status(),
    }
