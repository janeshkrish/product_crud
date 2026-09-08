from sqlalchemy.orm import Session
from models.category_model import Category
from request.category_request import CategoryCreateRequest

def create_category(
        db:Session,
        request: CategoryCreateRequest
):
    existing_category = (
        db.query(Category)
        .filter(
            Category.category_name == request.category_name
        )
        .first()
    )
    if existing_category:
        return None
    last_category = (
        db.query(Category)
        .order_by(Category.category_id.desc())
        .with_for_updates()
        .first()
    )
    if last_category:
        last_number = int(
            last_category.category_id.split("-")[1]
        )
        next_number = last_number + 1
    else:
        next_number = 1
    category_id = f"C-{next_number:02d}"
    category = Category(
        category_id = category_id,
        category_name = request.category_name,
        category_status = request.category_status
    )
    db.add(category)
    db.commit()
    db.refresh(category)

    return category
