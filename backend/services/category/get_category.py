from sqlalchemy.orm import Session
from models.category_model import Category

def get_categories(db:Session):
    return (
        db.query(Category)
        .order_by(Category.category_id)
        .all()
    )

def get_category(db:Session,category_id:str):
    return (
        db.query(Category)
        .filter(
            Category.category_id == category_id
        )
        .first()
    )
