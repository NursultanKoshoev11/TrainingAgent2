from fastapi import APIRouter, Query

from app.market_regime import classify_market_regime
from app.market_service import build_market_snapshot
from app.runtime_status import runtime_status
from app.scheduler import scheduler_status
from app.universe_service import analyze_universe

extra_router = APIRouter()


@extra_router.get('/api/runtime/status')
def runtime():
    return runtime_status()


@extra_router.get('/api/scheduler/status')
def scheduler():
    return scheduler_status()


@extra_router.get('/api/universe')
def universe(exchange: str = Query('binance'), timeframe: str = Query('1h'), limit: int = Query(10, ge=1, le=50)):
    return analyze_universe(exchange=exchange, timeframe=timeframe, limit=limit)


@extra_router.get('/api/market/regime')
def market_regime(symbol: str = Query('BTC/USDT'), exchange: str = Query('binance'), timeframe: str = Query('1h')):
    market = build_market_snapshot(symbol=symbol, exchange=exchange, timeframe=timeframe)
    return {'symbol': symbol, 'exchange': exchange, 'timeframe': timeframe, 'market_regime': classify_market_regime(market), 'market': market}
