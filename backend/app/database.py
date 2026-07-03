import os

from app.postgres_adapter import list_recent_advisory_signals_pg, postgres_enabled, postgres_status, save_advisory_signal_pg
from app.storage import recent_signals, save_signal


def database_mode():
    if postgres_enabled():
        return 'postgresql'
    return 'sqlite'


def save_advisory_signal(payload):
    if postgres_enabled():
        return save_advisory_signal_pg(payload)
    return save_signal(payload)


def list_recent_advisory_signals(limit=50):
    if postgres_enabled():
        return list_recent_advisory_signals_pg(limit=limit)
    return recent_signals(limit=limit)


def database_status():
    status = postgres_status()
    status['sqlite_file'] = 'advisor_signals.sqlite3'
    status['mode'] = database_mode()
    return status
