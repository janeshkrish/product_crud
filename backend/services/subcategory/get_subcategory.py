from sqlalchemy.orm import Session
from models.subcategory_model import Subcategory

def get_subcategoris(db:Session):
    return(
        db.query(Subcategory)
        .filter(
            Subcategory.deleted_at.is_(None)
        )
        .order_by(Subcategory.id)
        .all()
    )

def get_subcategory(db:Session,subcategory_id : str):
    return(
        db.query(Subcategory)
        .filter(
            Subcategory.subcategory_id == subcategory_id,
            Subcategory.deleted_at.is_(None)
        )
        .first()
    )