from fastapi import APIRouter, Query

from app.batch_pipeline import run_batch_pipeline
from app.context_registry import context_registry_status
from app.market_regime import classify_market_regime
from app.market_service import build_market_snapshot
from app.pipeline import run_symbol_pipeline
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


@extra_router.get('/api/context/status')
def context_status():
    return context_registry_status()


@extra_router.get('/api/universe')
def universe(exchange: str = Query('binance'), timeframe: str = Query('1h'), limit: int = Query(10, ge=1, le=50)):
    return analyze_universe(exchange=exchange, timeframe=timeframe, limit=limit)


@extra_router.get('/api/market/regime')
def market_regime(symbol: str = Query('BTC/USDT'), exchange: str = Query('binance'), timeframe: str = Query('1h')):
    market = build_market_snapshot(symbol=symbol, exchange=exchange, timeframe=timeframe)
    return {'symbol': symbol, 'exchange': exchange, 'timeframe': timeframe, 'market_regime': classify_market_regime(market), 'market': market}


@extra_router.get('/api/jobs/symbol')
def job_symbol(symbol: str = Query('BTC/USDT'), exchange: str = Query('binance'), timeframe: str = Query('1h'), save: bool = Query(True)):
    return run_symbol_pipeline(symbol=symbol, exchange=exchange, timeframe=timeframe, save=save)


@extra_router.get('/api/jobs/batch')
def job_batch(exchange: str = Query('binance'), timeframe: str = Query('1h'), limit: int = Query(10, ge=1, le=50), save: bool = Query(True)):
    return run_batch_pipeline(exchange=exchange, timeframe=timeframe, limit=limit, save=save)
