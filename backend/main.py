import logging
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from database import init_db
from routers import lessons, analysis, roadmap, profile
from routers.voice import router as voice_router
from agents.orchestrator import AgentOrchestrator
from agents.analyzer_agent import AnalyzerAgent
from agents.coach_agent import CoachAgent
from agents.dna_agent import DNAAgent
from agents.gamification_agent import GamificationAgent
from agents.report_agent import ReportAgent
from ws_manager import WebSocketManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    # Initialize WebSocket manager
    ws_manager = WebSocketManager()
    app.state.ws_manager = ws_manager

    # Initialize multi-agent orchestrator
    orchestrator = AgentOrchestrator()
    orchestrator.register(AnalyzerAgent(), ["transcript_chunk"])
    orchestrator.register(CoachAgent(), ["analysis_result"])
    orchestrator.register(DNAAgent(), ["analysis_result"])
    orchestrator.register(GamificationAgent(), ["analysis_result", "lesson_end"])
    orchestrator.register(ReportAgent(), ["lesson_end"])
    app.state.orchestrator = orchestrator

    logger.info("FluentAI backend started — orchestrator ready with 5 agents")
    yield
    logger.info("FluentAI backend shutting down")


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
app.include_router(voice_router)


@app.get("/api/health")
async def health():
    ws_count = app.state.ws_manager.active_connections if hasattr(app.state, "ws_manager") else 0
    return {"status": "ok", "ws_connections": ws_count}


@app.websocket("/ws/lesson/{lesson_id}")
async def websocket_endpoint(websocket: WebSocket, lesson_id: str):
    ws_manager: WebSocketManager = app.state.ws_manager
    await ws_manager.connect(lesson_id, websocket)
    try:
        while True:
            # Keep connection alive, receive any client messages
            data = await websocket.receive_text()
            logger.info(f"[WS] Received from client in lesson {lesson_id}: {data}")
    except WebSocketDisconnect:
        ws_manager.disconnect(lesson_id, websocket)
    except Exception:
        ws_manager.disconnect(lesson_id, websocket)
