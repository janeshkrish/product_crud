from sqlalchemy import Column, String, ForeignKey
from database import Base

class Product(Base):
    __tablename__ = "products"
    product_id = Column(
        String(20),
        primary_key = True,
        index = True
    )
    product_name = Column(
        String(100),
        nullable = False
    )
    category_name = Column(
        String(100),
        ForeignKey("categories.category_name",onupdate="CASCADE"),
        nullable = False
    )
    subcategory_name = Column(
        String(100),
        ForeignKey("subcategories.subcategory_name",onupdate="CASCADE"),
        nullable = False
    )
    product_status = Column(
        String(20),
        nullable = False,
        default = "Active"
    )
