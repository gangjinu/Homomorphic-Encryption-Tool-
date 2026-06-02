"""
Error handling middleware
"""

from fastapi import Request
from starlette.responses import JSONResponse
from app.core.logger import get_logger
from datetime import datetime

logger = get_logger(__name__)

async def error_handler_middleware(request: Request, call_next):
    """Global error handler middleware"""
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Unhandled error: {str(e)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error",
                "timestamp": datetime.utcnow().isoformat()
            }
        )
