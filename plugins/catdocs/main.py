import asyncio

from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from catdocs.service import service

from catdocs.endpoints.docs import router as docs_router

import settings

@asynccontextmanager
async def startup_event(*args, **kwargs):
    task = asyncio.create_task(service())
    yield
    # Shutdown event
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

app = FastAPI(
    lifespan=startup_event,
    root_path='/api/catdocs/v1'
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(docs_router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8002, host='0.0.0.0')