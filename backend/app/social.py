SOCIAL_SOURCES = [
    {'name': 'reddit', 'status': 'planned'},
    {'name': 'x_twitter', 'status': 'planned'},
    {'name': 'telegram_channels', 'status': 'planned'},
]


def social_status():
    return {
        'status': 'planned',
        'sources': SOCIAL_SOURCES,
        'note': 'Social sentiment is not connected yet. This module defines the future adapter contract.',
    }


def neutral_social_context():
    return {
        'social_score': 50,
        'social_flags': ['Social sentiment provider is not connected yet.'],
    }
