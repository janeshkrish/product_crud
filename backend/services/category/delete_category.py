from sqlalchemy.orm import Session
from models.category_model import Category
from models.product_model import Product
from models.subcategory_model import Subcategory
from datetime import datetime,timezone

def delete_category(db:Session,category_id:str):
    category = (
        db.query(Category)
        .filter(
            Category.category_id == category_id,
            Category.deleted_at.is_(None)
        )
        .first()
    )
    if not category:
        return None
    subcategory_exists = (
        db.query(Subcategory)
        .filter(
            Subcategory.category_name == category.category_name,
            Subcategory.deleted_at.is_(None)
        )
        .first()
    )
    if subcategory_exists:
        return "CATEGORY_IN_USE"
    
    product_exists = (
        db.query(Product)
        .filter(
            Product.category_name == category.category_name,
            Product.deleted_at.is_(None)
        )
        .first()
    )
    if product_exists:
        return "CATEGORY_IN_USE"
    category.deleted_at = datetime.now(timezone.utc)
    #db.delete(category)
    db.commit()
    db.refresh(category)
    return category