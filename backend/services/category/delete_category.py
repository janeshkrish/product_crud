from sqlalchemy.orm import Session
from models.category_model import Category
from models.product_model import Product
from models.subcategory_model import Subcategory

def delete_category(db:Session,category_id:str):
    category = (
        db.query(Category)
        .filter(Category.category_id == category_id)
        .first()
    )
    if not category:
        return None
    subcategory_exists = (
        db.query(Subcategory)
        .filter(Subcategory.category_name == category.category_name)
        .first()
    )
    if subcategory_exists:
        return "CATEGORY_IN_USE"
    product_exists = (
        db.query(Product)
        .filter(Product.category_name == category.category_name)
        .first()
    )
    if product_exists:
        return "CATEGORY_IN_USE"
    db.delete(category)
    db.commit()
    return category