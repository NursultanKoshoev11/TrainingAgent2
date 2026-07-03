from app.book_metrics import summarize_book
from app.streaming import normalize_stream_event, write_event_line

DEFAULT_FEED_FILE = 'market_feed_events.jsonl'


async def market_event_callback(event, receipt_timestamp):
    payload = {
        'exchange': getattr(event, 'exchange', None),
        'symbol': getattr(event, 'symbol', None),
        'receipt_timestamp': receipt_timestamp,
        'raw_type': event.__class__.__name__,
    }
    for field in ['price', 'amount', 'bid', 'ask', 'side']:
        if hasattr(event, field):
            value = getattr(event, field)
            try:
                value = float(value)
            except Exception:
                pass
            payload[field] = value
    normalized = normalize_stream_event(payload.get('exchange'), payload.get('symbol'), payload.get('raw_type'), payload)
    write_event_line(DEFAULT_FEED_FILE, normalized)


async def market_book_callback(book, receipt_timestamp):
    bids = []
    asks = []
    try:
        bids = list(book.book.bids.items())[:20]
        asks = list(book.book.asks.items())[:20]
    except Exception:
        pass
    payload = {
        'exchange': getattr(book, 'exchange', None),
        'symbol': getattr(book, 'symbol', None),
        'receipt_timestamp': receipt_timestamp,
        'book_summary': summarize_book(bids=bids, asks=asks),
    }
    normalized = normalize_stream_event(payload.get('exchange'), payload.get('symbol'), 'book', payload)
    write_event_line(DEFAULT_FEED_FILE, normalized)
