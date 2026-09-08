from sqlalchemy.orm import Session
from models.category_model import Category
from models.subcategory_model import Subcategory
from request.subcategory_request import SubcategoryCreateRequest

def create_subcategory(
        db:Session,
        request: SubcategoryCreateRequest
):
    category = (
        db.query(Category)
        .filter(
            Category.category_name == request.category_name,
            Category.deleted_at.is_(None)
        )
        .first()
    )
    if not category:
        return "CATEGORY_NOT_FOUND"
    existing_subcategory = (
        db.query(Subcategory)
        .filter(
            Subcategory.subcategory_name == request.subcategory_name,
            Subcategory.deleted_at.is_(None)
        )
        .first()
    )
    if existing_subcategory:
        return "SUBCATEGORY_ALREADY_EXISTS"
    
    last_subcategory = (
        db.query(Subcategory)
        .order_by(Subcategory.subcategory_id.desc())
        .wait_for_update()
        .first()
    )
    if last_subcategory:
        last_number = int(
            last_subcategory.subcategory_id.split("-")[1]
        )
        next_number = last_number + 1
    else:
        next_number = 1
    subcategory_id = f"S-{next_number:02d}"
    subcategory = Subcategory(
        subcategory_id = subcategory_id,
        subcategory_name = request.subcategory_name,
        category_name = request.category_name,
        subcategory_status = request.subcategory_status
    )
    db.add(subcategory)
    db.commit()
    db.refresh(subcategory)

    return subcategory
