from sqlalchemy import Session
from models.product_model import Product

def delete_product(db:Session,product_id: str):
    product = (
        db.query(Product)
        .filter(Product.product_id == product_id)
        .first()
    )
    if not product():
        return None
    db.delete(product)
    db.commit()
    return product

