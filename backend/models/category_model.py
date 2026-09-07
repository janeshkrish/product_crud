from sqlalchemy import Column, String
from database import Base

class Category(Base):
    __tablename__ = "categories"
    category_id = Column(
        String(20),
        primary_key = True,
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

