ANNOUNCEMENT_SOURCES = [
    {'name': 'binance_announcements', 'status': 'planned'},
    {'name': 'bybit_announcements', 'status': 'planned'},
    {'name': 'okx_announcements', 'status': 'planned'},
]


def announcements_status():
    return {
        'status': 'planned',
        'sources': ANNOUNCEMENT_SOURCES,
        'note': 'Announcement adapters should be used for listings, delistings, maintenance, and major exchange notices.',
    }


def normalize_announcement(source, title, url=None, published_at=None):
    return {
        'source': source,
        'title': title,
        'url': url,
        'published_at': published_at,
        'type': 'exchange_announcement',
    }
