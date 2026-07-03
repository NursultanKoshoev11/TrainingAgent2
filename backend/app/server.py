from fastapi import FastAPI

from app.api import router
from app.api_explain import explain_router
from app.api_extra import extra_router
from app.api_screener import screener_router

server = FastAPI()
server.include_router(router)
server.include_router(extra_router)
server.include_router(explain_router)
server.include_router(screener_router)
