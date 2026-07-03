from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.advice import router as advice_router
from app.routes.health import router as health_router
from app.routes.market import router as market_router
from app.routes.news import router as news_router

app = FastAPI(
    title="Crypto AI Advisor",
    description="Advisory-only crypto market intelligence API. It does not place trades.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(market_router, prefix="/api/market", tags=["market"])
app.include_router(news_router, prefix="/api/news", tags=["news"])
app.include_router(advice_router, prefix="/api", tags=["advice"])
