import os


def postgres_enabled():
    return os.getenv('DATABASE_URL', '').startswith('postgresql')


def postgres_status():
    return {
        'enabled': postgres_enabled(),
        'note': 'PostgreSQL adapter contract is reserved. SQLite remains the default local storage for now.',
    }


def save_payload(table_name, payload):
    raise NotImplementedError('PostgreSQL persistence is not implemented yet. Use SQLite local storage for the current MVP.')
