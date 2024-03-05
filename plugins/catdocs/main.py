import uvicorn
from fastapi import FastAPI

from catdocs.service import service


app = FastAPI()
@app.on_event("startup")
async def startup_event():
    await service()

if __name__ == '__main__':
    uvicorn.run("main:app", port=8002)