import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from catdocs.service import service

from catdocs.endpoints.docs import router as docs_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(docs_router)
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(service())

if __name__ == '__main__':
    uvicorn.run("main:app", port=8002)