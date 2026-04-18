import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from database import init_db
from routers import lessons, analysis, roadmap, profile


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    # TODO: register agents in P03
    yield


app = FastAPI(title="FluentAI Backend", version="0.1.0", lifespan=lifespan)

origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lessons.router)
app.include_router(analysis.router)
app.include_router(roadmap.router)
app.include_router(profile.router)


@app.get("/api/health")
async def health():
    return {"status": "ok"}
