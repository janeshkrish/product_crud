from sqlalchemy import Column,String,ForeignKey
from database import Base

class Subcategory(Base):
    __tablename__ = "subcategories"
    subcategory_id = Column(
        String(20),
        primary_key = True,
        index = True
    )
    subcategory_name = Column(
        String(100),
        nullable = False,
        unique = True
    )
    category_name = Column(
        String(100),
        ForeignKey("categories.category_name",deferrable = True,initially="DEFERRED"),
        nullable = False
    )
    subcategory_status = Column(
        String(20),
        nullable = False,
        default = "Active"
    )
