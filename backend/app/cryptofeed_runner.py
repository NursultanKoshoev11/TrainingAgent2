from app.feed_callbacks import market_book_callback, market_event_callback
from app.settings import symbol_list


def run_cryptofeed():
    try:
        from cryptofeed import FeedHandler
        from cryptofeed.defines import L2_BOOK, TICKER, TRADES
        from cryptofeed.exchanges import Binance, Bybit
    except ImportError as exc:
        raise RuntimeError('cryptofeed is not installed. Install backend optional dependency: streaming.') from exc

    feed_handler = FeedHandler()
    symbols = symbol_list()
    feed_handler.add_feed(Binance(symbols=symbols, channels=[TRADES, TICKER], callbacks={TRADES: market_event_callback, TICKER: market_event_callback}))
    feed_handler.add_feed(Bybit(symbols=symbols, channels=[TRADES, TICKER], callbacks={TRADES: market_event_callback, TICKER: market_event_callback}))
    feed_handler.add_feed(Binance(symbols=symbols[:3], channels=[L2_BOOK], callbacks={L2_BOOK: market_book_callback}))
    feed_handler.run()


if __name__ == '__main__':
    run_cryptofeed()
