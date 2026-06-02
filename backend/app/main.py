"""
FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.logger import setup_logging
from app.api.v1.router import api_router
from app.middleware.error_handler import error_handler_middleware
from app.middleware.security import security_middleware

# Setup logging
setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events for FastAPI"""
    # Startup
    print("🚀 SecureML Cloud starting...")
    yield
    # Shutdown
    print("🛑 SecureML Cloud shutting down...")

app = FastAPI(
    title="SecureML Cloud API",
    description="Secure Machine Learning with Homomorphic Encryption",
    version="1.0.0",
    lifespan=lifespan
)

# Security Middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Middleware
app.middleware("http")(error_handler_middleware)
app.middleware("http")(security_middleware)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "SecureML Cloud"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "SecureML Cloud API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
