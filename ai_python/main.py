from http.client import responses

# from binstar_client import STATUS_CODE
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

import logging

from starlette.requests import Request
from starlette.responses import Response

app = FastAPI(
    title='My API',
    description='sample api',
    version='0.0.1',
    docs_url=None,
    redoc_url=None
)

@app.get('/')
async def read_root():
    return {'hello' : 'world'}

class LoggingMiddleware(BaseHTTPMiddleware):
    logging.basicConfig(level=logging.INFO)

    async def dispatch(self, request, call_next):
        logging.info(f"Req : {request.method} - {request.url}")
        response = await call_next(request)
        logging.info(f"Status Code : {response.status_code}")

        return response

app.add_middleware(LoggingMiddleware)

class Item(BaseModel):
    name : str
    description : str = None
    price : float
    tax : float = None

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id" : item_id, "q" : q}

@app.post("/items")
async def create_item(item: Item):
    return item

