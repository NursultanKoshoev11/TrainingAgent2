REGULATORY_SOURCES = [
    {'name': 'sec', 'status': 'planned'},
    {'name': 'cftc', 'status': 'planned'},
    {'name': 'eu_esma', 'status': 'planned'},
    {'name': 'uk_fca', 'status': 'planned'},
]


def regulatory_status():
    return {
        'status': 'planned',
        'sources': REGULATORY_SOURCES,
        'note': 'Regulatory headline adapters are planned for macro/event risk context.',
    }


def normalize_regulatory_item(source, title, url=None, published_at=None):
    return {
        'source': source,
        'title': title,
        'url': url,
        'published_at': published_at,
        'type': 'regulatory_news',
    }
