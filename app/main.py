from fastapi import FastAPI
from app.api.kakao import router as kakao_router

app = FastAPI()

app.include_router(kakao_router)
