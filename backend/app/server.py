from fastapi import FastAPI

from app.api import router

server = FastAPI()
server.include_router(router)
