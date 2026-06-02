"""
Logging configuration
"""

import logging
import sys
from app.core.config import settings

def setup_logging():
    """Configure logging for the application"""
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, settings.LOG_LEVEL))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, settings.LOG_LEVEL))
    
    # Formatter
    formatter = logging.Formatter(settings.LOG_FORMAT)
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    if not logger.handlers:
        logger.addHandler(console_handler)
    
    return logger

def get_logger(name: str) -> logging.Logger:
    """Get a logger instance"""
    return logging.getLogger(name)
