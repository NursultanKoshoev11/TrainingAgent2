import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import router
from app.api_explain import explain_router
from app.api_extra import extra_router
from app.api_screener import screener_router


def cors_origins():
    value = os.getenv('CORS_ORIGINS', 'http://localhost:3000')
    return [item.strip() for item in value.split(',') if item.strip()]


server = FastAPI(title='Crypto AI Advisor', version='0.1.0')
server.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins(),
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
server.include_router(router)
server.include_router(extra_router)
server.include_router(explain_router)
server.include_router(screener_router)
