import json
import sqlite3
from pathlib import Path

DB_PATH = Path('advisor_signals.sqlite3')


def connect():
    connection = sqlite3.connect(DB_PATH)
    connection.execute(
        '''
        create table if not exists advisory_signals (
            id integer primary key autoincrement,
            symbol text not null,
            recommendation text not null,
            final_score real not null,
            risk_score real not null,
            payload text not null,
            created_at datetime default current_timestamp
        )
        '''
    )
    return connection


def save_signal(payload):
    with connect() as connection:
        cursor = connection.execute(
            'insert into advisory_signals (symbol, recommendation, final_score, risk_score, payload) values (?, ?, ?, ?, ?)',
            (
                payload.get('symbol'),
                payload.get('recommendation'),
                payload.get('final_score'),
                payload.get('risk_score'),
                json.dumps(payload),
            ),
        )
        return cursor.lastrowid


def recent_signals(limit=50):
    with connect() as connection:
        rows = connection.execute(
            'select id, symbol, recommendation, final_score, risk_score, payload, created_at from advisory_signals order by id desc limit ?',
            (limit,),
        ).fetchall()
    return [
        {
            'id': row[0],
            'symbol': row[1],
            'recommendation': row[2],
            'final_score': row[3],
            'risk_score': row[4],
            'payload': json.loads(row[5]),
            'created_at': row[6],
        }
        for row in rows
    ]
