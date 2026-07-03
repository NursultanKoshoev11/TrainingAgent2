from fastapi import APIRouter, Query

from app.advice_explainer import explain_full_advice
from app.advice_service import build_advice

explain_router = APIRouter()


@explain_router.get('/api/advice/explain')
def explain_advice_route(symbol: str = Query('BTC/USDT'), exchange: str = Query('binance'), timeframe: str = Query('1h')):
    advice = build_advice(symbol=symbol, exchange=exchange, timeframe=timeframe)
    return explain_full_advice(advice)
