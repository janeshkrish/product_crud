import uuid 
from sqlalchemy import Column, String, ForeignKey, func,DateTime
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(
        UUID(as_uuid=True),
        primary_key = True,
        default = uuid.uuid4,   
        index = True
    )
    product_id = Column(
        String(20),
        unique = True,
        nullable = False,
        index = True
    )
    product_name = Column(
        String(100),
        nullable = False
    )
    category_name = Column(
        String(100),
        ForeignKey("categories.category_name",deferrable = True,initially="DEFERRED"),
        nullable = False
    )
    subcategory_name = Column(
        String(100),
        ForeignKey("subcategories.subcategory_name",deferrable = True,initially="DEFERRED"),
        nullable = False
    )
    product_status = Column(
        String(20),
        nullable = False,
        default = "Active"
    )
    created_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
        nullable = False
    )
    deleted_at = Column(
        DateTime(timezone = True),
        server_default = func.now(),
        onupdate = func.now(),
        nullable = False
    )
    deleted_at = Column(
        DateTime(timezone = True),
        nullable = True
    )
