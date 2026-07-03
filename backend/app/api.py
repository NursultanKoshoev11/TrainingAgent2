from fastapi import APIRouter, Query

from app.advice_service import build_advice
from app.database import database_status, list_recent_advisory_signals, save_advisory_signal
from app.market_service import build_market_snapshot
from app.news_data import latest_news
from app.overview_service import build_overview
from app.sentiment import enrich_news
from app.streaming import streaming_status
from app.watchlist import get_watchlist

router = APIRouter()


@router.get('/ping')
def ping():
    return {'ok': True, 'mode': 'advisory-only'}


@router.get('/api/watchlist')
def watchlist():
    return get_watchlist()


@router.get('/api/database/status')
def db_status():
    return database_status()


@router.get('/api/streaming/status')
def stream_status():
    return streaming_status()


@router.get('/api/market/snapshot')
def market_snapshot(symbol: str = Query('BTC/USDT'), exchange: str = Query('binance'), timeframe: str = Query('1h')):
    return build_market_snapshot(symbol=symbol, exchange=exchange, timeframe=timeframe)


@router.get('/api/news/latest')
def news_latest(symbol: str = Query('BTC/USDT'), limit: int = Query(12, ge=1, le=50)):
    return {'symbol': symbol, 'items': enrich_news(latest_news(symbol=symbol, limit=limit))}


@router.get('/api/advice')
def advice(symbol: str = Query('BTC/USDT'), exchange: str = Query('binance'), timeframe: str = Query('1h'), save: bool = Query(False)):
    result = build_advice(symbol=symbol, exchange=exchange, timeframe=timeframe)
    if save:
        result['saved_signal_id'] = save_advisory_signal(result)
    return result


@router.get('/api/overview')
def overview(exchange: str = Query('binance'), timeframe: str = Query('1h')):
    return build_overview(exchange=exchange, timeframe=timeframe)


@router.get('/api/signals/recent')
def signals_recent(limit: int = Query(50, ge=1, le=200)):
    return {'items': list_recent_advisory_signals(limit=limit)}
