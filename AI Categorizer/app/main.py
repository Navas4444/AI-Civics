"""
Main FastAPI application.
"""
from app.routers.complaints import router as complaints_router
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.database.database import Base
from app.database.database import engine
from app.database import models   # noqa: F401
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.ai.gemini_client import GeminiClient
from app.limiter import limiter
from app.routers.classify import router as classify_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="AI Categorizer API",
    description="AI Backend for Civic Complaint Management System",
    version="1.0.0",
)
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads",
)
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Configure rate limiter
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Register routers
app.include_router(classify_router)
app.include_router(complaints_router)

# Gemini client
gemini = GeminiClient()


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(
    request: Request,
    exc: RateLimitExceeded,
):
    return JSONResponse(
        status_code=429,
        content={
            "detail": (
                "Too many requests. "
                "Please wait a minute."
            )
        },
    )


@app.get("/")
def root():
    return {
        "message": "AI Categorizer Backend is running successfully!",
        "status": "success",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "gemini": "configured",
    }


@app.get("/test-gemini")
def test_gemini():
    try:
        response = gemini.client.models.generate_content(
            model=gemini.model,
            contents="Reply with exactly: Gemini connection successful.",
        )

        return {
            "success": True,
            "response": response.text.strip(),
        }

    except Exception as exc:
        return {
            "success": False,
            "error": str(exc),
        }