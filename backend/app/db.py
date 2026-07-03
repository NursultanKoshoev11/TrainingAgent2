import json
import os
import sqlite3
from pathlib import Path

from app.db_schema import SCHEMA_SQL
from app.postgres_adapter import postgres_enabled, save_market_snapshot_pg, save_news_items_pg

DB_PATH = Path(os.getenv('ADVISOR_DB_PATH', 'advisor_data.sqlite3'))


def connect():
    connection = sqlite3.connect(DB_PATH)
    for statement in SCHEMA_SQL:
        connection.execute(statement)
    return connection


def insert_market_snapshot(snapshot):
    if postgres_enabled():
        return save_market_snapshot_pg(snapshot)
    with connect() as connection:
        cursor = connection.execute(
            'insert into market_snapshots (exchange, symbol, timeframe, latest_price, market_score, volatility_percent, volume_ratio, payload) values (?, ?, ?, ?, ?, ?, ?, ?)',
            (
                snapshot.get('exchange'),
                snapshot.get('symbol'),
                snapshot.get('timeframe'),
                snapshot.get('latest_price'),
                snapshot.get('score'),
                snapshot.get('volatility_percent'),
                snapshot.get('volume_ratio'),
                json.dumps(snapshot),
            ),
        )
        return cursor.lastrowid


def insert_news_items(symbol, items):
    if postgres_enabled():
        return save_news_items_pg(symbol, items)
    ids = []
    with connect() as connection:
        for item in items:
            cursor = connection.execute(
                'insert into news_items (symbol, title, url, source, published_at, payload) values (?, ?, ?, ?, ?, ?)',
                (symbol, item.get('title'), item.get('url'), item.get('source'), item.get('published_at'), json.dumps(item)),
            )
            ids.append(cursor.lastrowid)
    return ids
