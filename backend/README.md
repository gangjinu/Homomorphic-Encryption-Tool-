# Backend Setup Guide

## Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Virtual Environment Tool (venv or conda)

## Installation

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Run database migrations
alembic upgrade head

# Start the development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Environment Variables

Create a `.env` file:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/secureml
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Redis
REDIS_URL=redis://localhost:6379

# JWT
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# HE Configuration
HE_SCHEME=CKKS
HE_N=16384
HE_SCALE=2147483648

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/1

# S3/Storage
S3_BUCKET=secureml-models
S3_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret

# Security
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ORIGINS=http://localhost:3000

# Logging
LOG_LEVEL=INFO
```

## API Documentation

Start the server and visit: `http://localhost:8000/docs`

## Testing

```bash
pytest tests/ -v
pytest tests/ --cov=app
```
