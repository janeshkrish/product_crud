from sqlalchemy.orm import Session
from models.subcategory_model import Subcategory

def get_subcategoris(db:Session):
    return(
        db.query(Subcategory)
        .order_by(Subcategory.subcategory_id)
        .all()
    )

def get_subcategory(db:Session,subcategory_id : str):
    return(
        db.query(Subcategory)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .first()
    )