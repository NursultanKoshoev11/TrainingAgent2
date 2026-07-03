import json
import os
import time

from app.overview_service import build_overview
from app.settings import DEFAULT_EXCHANGE, DEFAULT_TIMEFRAME
from app.storage import save_signal


def scheduler_config():
    return {
        'market_interval_seconds': int(os.getenv('MARKET_INTERVAL_SECONDS', '300')),
        'news_interval_seconds': int(os.getenv('NEWS_INTERVAL_SECONDS', '300')),
        'overview_interval_seconds': int(os.getenv('OVERVIEW_INTERVAL_SECONDS', '900')),
        'save_signals': os.getenv('SAVE_SCHEDULED_SIGNALS', 'true').lower() == 'true',
        'exchange': os.getenv('DEFAULT_EXCHANGE', DEFAULT_EXCHANGE),
        'timeframe': os.getenv('DEFAULT_TIMEFRAME', DEFAULT_TIMEFRAME),
    }


def scheduler_status():
    return {'mode': os.getenv('SCHEDULER_MODE', 'manual-worker'), 'config': scheduler_config()}


def run_advisory_cycle(exchange=DEFAULT_EXCHANGE, timeframe=DEFAULT_TIMEFRAME, save=True):
    overview = build_overview(exchange=exchange, timeframe=timeframe)
    saved = []
    if save:
        for item in overview.get('items', []):
            if 'recommendation' in item:
                saved.append(save_signal(item))
    return {'overview': overview, 'saved_signal_ids': saved}


def run_cycle_from_config():
    config = scheduler_config()
    return run_advisory_cycle(exchange=config['exchange'], timeframe=config['timeframe'], save=config['save_signals'])


def run_forever():
    config = scheduler_config()
    while True:
        result = run_cycle_from_config()
        print(json.dumps(result, indent=2))
        time.sleep(config['market_interval_seconds'])


if __name__ == '__main__':
    run_forever()
