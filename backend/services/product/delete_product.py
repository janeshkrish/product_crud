from datetime import timezone, datetime
from sqlalchemy.orm import Session
from models.product_model import Product

def delete_product(db:Session,product_id: str):
    product = (
        db.query(Product)
        .filter(
            Product.product_id == product_id,
            Product.deleted_at.is_(None)
        )
        .first()
    )
    if not product:
        return None
    product.delete_at = datetime.now(timezone.utc)
    #db.delete(product)
    db.commit()
    db.refresh(product)
    return product

