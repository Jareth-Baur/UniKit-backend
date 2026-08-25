from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    background,
    ocr,
    transcription
)


app = FastAPI(
    title="UniKit API",
    description="Free utilities for everyone.",
    version="1.0.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Routers
# --------------------------------------------------

app.include_router(
    background.router
)

app.include_router(
    ocr.router
)

app.include_router(
    transcription.router
)


# --------------------------------------------------
# Root
# --------------------------------------------------

@app.get("/")
async def root():

    return {
        "name": "UniKit API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }