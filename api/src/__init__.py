from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.users.router import user_app

app = FastAPI(title="python-fastapi-restapi", version='0.1')
app.include_router(user_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
