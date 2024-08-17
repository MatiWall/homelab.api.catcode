import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dependecies.endpoints import router

app = FastAPI(
    root_path='/api/dependencies/v1'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, host='0.0.0.0')