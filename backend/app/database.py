import os

from app.storage import recent_signals, save_signal


def database_mode():
    url = os.getenv('DATABASE_URL', '')
    if url.startswith('postgresql'):
        return 'postgresql_planned'
    return 'sqlite'


def save_advisory_signal(payload):
    return save_signal(payload)


def list_recent_advisory_signals(limit=50):
    return recent_signals(limit=limit)


def database_status():
    return {
        'mode': database_mode(),
        'sqlite_file': 'advisor_signals.sqlite3',
        'postgresql_note': 'Set DATABASE_URL to enable future PostgreSQL adapter work.'
    }
