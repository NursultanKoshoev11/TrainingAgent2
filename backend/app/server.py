from fastapi import FastAPI

from app.api import router
from app.api_extra import extra_router

server = FastAPI()
server.include_router(router)
server.include_router(extra_router)
