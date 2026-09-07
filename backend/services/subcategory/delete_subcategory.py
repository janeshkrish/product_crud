from sqlalchemy import Session
from models.subcategory_model import Subcategory
from models.product_model import Product

def delete_subcategory(db:Session,subcategory_id : str):
    subcategory = (
        db.query(Subcategory)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .first()
    )
    if not subcategory:
        return None
    product_exists = (
        db.query(Product)
        .filter(Product.product_name == subcategory.subcategory_name)
        .first()
    )
    if product_exists:
        return "SUBCATEGORY_IN_USE"
    db.delete(subcategory)
    db.commit()
    return subcategory
