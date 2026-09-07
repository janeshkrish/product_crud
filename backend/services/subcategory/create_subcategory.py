from sqlalchemy.orm import Session
from models.category_model import Category
from response.subcategory_response import SubcategoryResponse 
from models.subcategory_model import Subcategory

def create_subcategory(
        db:Session,
        request: SubcategoryResponse
):
    category = (
        db.query(Category)
        .filter(
            Category.category_name == request.category_name
        )
        .first()
    )
    if not category:
        return None
    existing_subcategory = (
        db.query(Subcategory)
        .filter(
            Subcategory.subcategory_name == request.subcategory_name
        )
        .first()
    )
    if existing_subcategory:
        return None
    last_subcategory = (
        db.query(Subcategory)
        .order_by(Subcategory.subcategory_id.desc())
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
