from sqlalchemy.orm import Session
from models.category_model import Category
from models.product_model import Product
from models.subcategory_model import Subcategory
from request.category_request import CategoryUpdateRequest

def update_category(
        db:Session,
        category_id: str,
        request : CategoryUpdateRequest
):
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
    if request.category_name and request.category_name != category.category_name:
        existing_category = (
            db.query(Category)
            .filter(
                Category.category_name == request.category_name,
                Category.category_id != category_id,
                Category.deleted_at.is_(None)
            )
            .first()
        )
        if existing_category:
            return "CATEGORY_ALREADY_EXIT"
        old_category_name = category.category_name
        #category.category_name = request.category_name 
        db.query(Subcategory).filter(
            Subcategory.category_name == old_category_name
        ).update(
            {
                Subcategory.category_name : request.category_name
            },
            synchronize_session = False
        )
        db.query(Product).filter(
            Product.category_name == old_category_name
        ).update(
            {
                Product.category_name : request.category_name
            },
            synchronize_session = False
        )
    update_data = request.model_dump(exclude_unset = True)
    for field,value in update_data.items():
        setattr(category,field,value)
    ##if request.category_status:
    ##  category.category_status = request.category_status
    db.commit()
    db.refresh(category)
    return category