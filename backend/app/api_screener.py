from fastapi import APIRouter, Query

from app.screener import screen_market

screener_router = APIRouter()


@screener_router.get('/api/screener')
def screener(exchange: str = Query('binance'), timeframe: str = Query('1h'), limit: int = Query(10, ge=1, le=50)):
    return screen_market(exchange=exchange, timeframe=timeframe, limit=limit)
