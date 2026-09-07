from sqlalchemy.orm import Session
from models.product_model import Product

def get_Products(db:Session):
    return (
        db.query(Product)
        .order_by(Product.product_id)
        .all()
    )

def get_Product(db:Session,product_id:str):
    return (
        db.query(Product)
        .filter(Product.product_id == product_id)
        .first()
    )
