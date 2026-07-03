import json
import time

from app.advice_service import build_advice
from app.settings import DEFAULT_EXCHANGE, DEFAULT_TIMEFRAME, symbol_list


def run_once():
    results = []
    for symbol in symbol_list():
        try:
            results.append(build_advice(symbol=symbol, exchange=DEFAULT_EXCHANGE, timeframe=DEFAULT_TIMEFRAME))
        except Exception as error:
            results.append({'symbol': symbol, 'error': str(error)})
    return results


def main(interval_seconds=300):
    while True:
        print(json.dumps(run_once(), indent=2))
        time.sleep(interval_seconds)


if __name__ == '__main__':
    main()
