import time

from app.overview_service import build_overview
from app.settings import DEFAULT_EXCHANGE, DEFAULT_TIMEFRAME
from app.storage import save_signal


def run_advisory_cycle(exchange=DEFAULT_EXCHANGE, timeframe=DEFAULT_TIMEFRAME, save=True):
    overview = build_overview(exchange=exchange, timeframe=timeframe)
    saved = []
    if save:
        for item in overview.get('items', []):
            if 'recommendation' in item:
                saved.append(save_signal(item))
    return {'overview': overview, 'saved_signal_ids': saved}


def run_forever(interval_seconds=300):
    while True:
        result = run_advisory_cycle(save=True)
        print(result)
        time.sleep(interval_seconds)


if __name__ == '__main__':
    run_forever()
