from app.exchange_announcements import announcements_status
from app.gdelt_adapter import gdelt_status
from app.macro_adapters import macro_adapters_status
from app.regulatory_news import regulatory_status
from app.social_adapters import social_adapters_status


def context_registry_status():
    return {
        'gdelt': gdelt_status(),
        'exchange_announcements': announcements_status(),
        'regulatory_news': regulatory_status(),
        'macro_adapters': macro_adapters_status(),
        'social_adapters': social_adapters_status(),
    }
