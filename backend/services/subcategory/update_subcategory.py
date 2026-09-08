from sqlalchemy.orm import Session
from models.category_model import Category
from models.subcategory_model import Subcategory
from models.product_model import Product
from request.subcategory_request import SubcategoryUpdateRequest

def update_subcategory(
        db:Session,
        subcategory_id : str,
        request: SubcategoryUpdateRequest
):
    subcategory = (
        db.query(Subcategory)
        .filter(
            Subcategory.subcategory_id == subcategory_id
        )
        .first()
    )
    if not subcategory:
        return None
    if request.category_name:
        category = (
            db.query(Category)
            .filter(
                Category.category_name == request.category_name
            )
            .first()
        )
        if not category:
            return "CATEGORY_NOT_FOUND"
    existing_subcategory = None
    if request.subcategory_name:
        existing_subcategory = (
            db.query(Subcategory)
            .filter(
                Subcategory.subcategory_name == request.subcategory_name,
                Subcategory.subcategory_id != subcategory_id
            )
            .first()
            )
        if existing_subcategory:
            return "SUBCATEGORY_ALREADY_EXISTS"
        oldsubcategory_name = subcategory.subcategory_name
        if request.subcategory_name:
            subcategory.subcategory_name = request.subcategory_name
        #subcategory.subcategory_name = request.subcategory_name
        db.query(Product).filter(
            Product.subcategory_name == oldsubcategory_name 
            ).update(
            {
            Product.subcategory_name : request.subcategory_name
            },
            synchronize_session = False
            )
    if request.category_name:
        subcategory.category_name = request.category_name
    if request.subcategory_status:
        subcategory.subcategory_status = request.subcategory_status
    db.commit()
    db.refresh(subcategory)
    return subcategory