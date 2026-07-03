from app.database import database_status
from app.provider_health import provider_health
from app.scheduler import scheduler_status
from app.streaming import streaming_status
from app.watchlist import get_watchlist


def runtime_status():
    return {
        'watchlist': get_watchlist(),
        'database': database_status(),
        'providers': provider_health(),
        'scheduler': scheduler_status(),
        'streaming': streaming_status(),
    }
