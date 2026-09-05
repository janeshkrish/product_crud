from sqlalchemy import Column , String , Float
from database import Base

class Product(Base):
    __tablename__ = "products"
    product_id = Column(
        String,
        primary_key = True,
        index = True
    )
    product_name = Column(
        String,
        nullable = False
    )
    product_image = Column(
        String,
        nullable = True
    )
    product_price = Column(
        Float,
        nullable = False
    )
    product_status = Column(
        String,
        nullable = False,
        default = "Active"
    )