from sqlalchemy.orm import Session
from models.subcategory_model import Subcategory
from models.product_model import Product
from datetime import datetime,timezone

def delete_subcategory(db:Session,subcategory_id : str):
    subcategory = (
        db.query(Subcategory)
        .filter(
            Subcategory.subcategory_id == subcategory_id,
            Subcategory.deleted_at.is_(None)
        )
        .first()
    )
    if not subcategory:
        return None
    product_exists = (
        db.query(Product)
        .filter(
            Product.product_name == subcategory.subcategory_name,
            Product.deleted_at.is_(None)
        )
        .first()
    )
    if product_exists:
        return "SUBCATEGORY_IN_USE"
    subcategory.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(subcategory)
    return subcategory
