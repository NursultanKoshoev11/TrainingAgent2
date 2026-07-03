SCHEMA_SQL = [
    '''
    create table if not exists market_snapshots (
        id integer primary key autoincrement,
        exchange text not null,
        symbol text not null,
        timeframe text not null,
        latest_price real,
        market_score real,
        volatility_percent real,
        volume_ratio real,
        payload text not null,
        created_at datetime default current_timestamp
    )
    ''',
    '''
    create table if not exists news_items (
        id integer primary key autoincrement,
        symbol text not null,
        title text not null,
        url text,
        source text,
        published_at text,
        payload text not null,
        created_at datetime default current_timestamp
    )
    ''',
    '''
    create table if not exists sentiment_scores (
        id integer primary key autoincrement,
        news_item_id integer,
        label text not null,
        score real not null,
        confidence real not null,
        engine text,
        created_at datetime default current_timestamp
    )
    ''',
    '''
    create table if not exists risk_flags (
        id integer primary key autoincrement,
        signal_id integer,
        flag text not null,
        created_at datetime default current_timestamp
    )
    ''',
]
