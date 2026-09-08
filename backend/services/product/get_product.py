from sqlalchemy.orm import Session
from models.product_model import Product

def get_Products(db:Session):
    return (
        db.query(Product)
        .filter(
            Product.deleted_at.is_(None)
        )
        .order_by(Product.id)
        .all()
    )

def get_Product(db:Session,product_id:str):
    return (
        db.query(Product)
        .filter(
            Product.product_id == product_id,
            Product.deleted_at.is_(None)
        )
        .first()
    )
