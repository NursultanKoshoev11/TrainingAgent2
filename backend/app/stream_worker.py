import time

from app.market_service import build_market_snapshot
from app.settings import DEFAULT_EXCHANGE, DEFAULT_TIMEFRAME
from app.streaming import normalize_stream_event, stream_config, write_event_line


def run_stream_poll(output_path='stream_events.jsonl'):
    config = stream_config()
    interval = config['poll_interval_seconds']
    while True:
        for symbol in config['symbols']:
            try:
                snapshot = build_market_snapshot(symbol=symbol, exchange=DEFAULT_EXCHANGE, timeframe=DEFAULT_TIMEFRAME)
                event = normalize_stream_event(DEFAULT_EXCHANGE, symbol, 'market_snapshot', snapshot)
                write_event_line(output_path, event)
                print(event)
            except Exception as error:
                print({'symbol': symbol, 'error': str(error)})
        time.sleep(interval)


if __name__ == '__main__':
    run_stream_poll()
