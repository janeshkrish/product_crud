import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(
        UUID(as_uuid = True),
        primary_key = True,
        default = uuid.uuid4,
        index = True
    )
    category_id = Column(
        String(20),
        unique = True,
        nullable = False,
        index = True
    )
    category_name = Column(
        String(100),
        nullable = False,
        unique = True
    )
    category_status = Column(
        String(20),
        nullable = False,
        default = "Active"
    )
    created_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
        nullable = False
    )
    updated_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
        onupdate = func.now(),
        nullable = False
    )
    deleted_at = Column(
        DateTime(timezone = True),
        nullable = True
    )

