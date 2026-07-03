from fastapi import APIRouter, Query

from app.batch_pipeline import run_batch_pipeline
from app.pipeline import run_symbol_pipeline

pipeline_router = APIRouter()


@pipeline_router.get('/api/pipeline/symbol')
def pipeline_symbol(symbol: str = Query('BTC/USDT'), exchange: str = Query('binance'), timeframe: str = Query('1h'), save: bool = Query(True)):
    return run_symbol_pipeline(symbol=symbol, exchange=exchange, timeframe=timeframe, save=save)


@pipeline_router.get('/api/pipeline/batch')
def pipeline_batch(exchange: str = Query('binance'), timeframe: str = Query('1h'), limit: int = Query(10, ge=1, le=50), save: bool = Query(True)):
    return run_batch_pipeline(exchange=exchange, timeframe=timeframe, limit=limit, save=save)
