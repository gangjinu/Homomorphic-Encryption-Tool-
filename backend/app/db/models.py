"""
Database models for SecureML Cloud
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean, Float, ForeignKey, LargeBinary, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from datetime import datetime
import enum
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    echo=settings.DEBUG
)

Base = declarative_base()

class UserRole(str, enum.Enum):
    """User roles"""
    ADMIN = "admin"
    DATA_OWNER = "data_owner"
    ANALYST = "analyst"

class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(Enum(UserRole), default=UserRole.ANALYST)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    models = relationship("Model", back_populates="owner")
    predictions = relationship("Prediction", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")

class Model(Base):
    """ML Model model"""
    __tablename__ = "models"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    model_name = Column(String, nullable=False)
    model_version = Column(String, default="1.0.0")
    description = Column(Text, nullable=True)
    model_type = Column(String, nullable=False)  # linear_regression, logistic_regression, neural_network
    model_file_path = Column(String, nullable=True)  # S3 path
    model_size = Column(Integer, nullable=True)  # in bytes
    input_features = Column(Integer, nullable=False)
    output_type = Column(String, nullable=False)  # regression, classification
    is_encrypted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    owner = relationship("User", back_populates="models")
    predictions = relationship("Prediction", back_populates="model")

class Prediction(Base):
    """Prediction history model"""
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.id"), nullable=False)
    encrypted_input = Column(LargeBinary, nullable=True)
    encrypted_output = Column(LargeBinary, nullable=True)
    decrypted_output = Column(Float, nullable=True)
    execution_time = Column(Float, nullable=True)  # in milliseconds
    computation_depth = Column(Integer, nullable=True)
    noise_budget = Column(Float, nullable=True)
    status = Column(String, default="completed")  # completed, failed, pending
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="predictions")
    model = relationship("Model", back_populates="predictions")

class EncryptionKey(Base):
    """Encryption key management"""
    __tablename__ = "encryption_keys"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    public_key = Column(LargeBinary, nullable=False)
    rotation_key = Column(LargeBinary, nullable=True)
    key_scheme = Column(String, nullable=False)  # CKKS
    key_size = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AuditLog(Base):
    """Audit logging for compliance"""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String, nullable=False)  # create, read, update, delete, encrypt, decrypt
    resource_type = Column(String, nullable=False)  # model, prediction, key
    resource_id = Column(Integer, nullable=True)
    details = Column(Text, nullable=True)
    ip_address = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    status = Column(String, nullable=False)  # success, failure
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="audit_logs")

class SystemMetrics(Base):
    """System performance and resource metrics"""
    __tablename__ = "system_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cpu_usage = Column(Float, nullable=True)
    memory_usage = Column(Float, nullable=True)
    active_predictions = Column(Integer, nullable=True)
    total_predictions = Column(Integer, nullable=True)
    average_computation_time = Column(Float, nullable=True)
    error_rate = Column(Float, nullable=True)

def get_db():
    """Database session dependency"""
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
