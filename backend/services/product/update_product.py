from sqlalchemy.orm import Session
from models.product_model import Product
from models.subcategory_model import Subcategory
from models.category_model import Category
from request.product_request import ProductUpdateRequest

def update_product(
        db:Session,
        request: ProductUpdateRequest,
        product_id : str
):
    product = (
        db.query(Product)
        .filter(
            Product.product_id == product_id,
            Product.deleted_at.is_(None)
        )
        .first()
    )
    if not product:
        return None
    update_data = request.model_dump(exclude_unset = True)
    new_category_name = update_data.get("category_name",product.category_name)
    new_subcategory_name = update_data.get("subcategory_name",product.subcategory_name)
    # category_name = (
    #     request.category_name
    #     if request.category_name
    #     else product.category_name
    # )
    # subcategory_name = (
    #     request.subcategory_name
    #     if request.subcategory_name
    #     else product.subcategory_name
    # )
    if "category_name" in update_data or "subcategory_name" in update_data:
        category = (
            db.query(Category)
            .filter(
                Category.category_name == new_category_name,
                Category.deleted_at.is_(None)
            ).first()
        )
        if not category:
            return "CATEGORY_NOT_FOUND"
        subcategory = (
            db.query(Subcategory)
            .filter(
                Subcategory.subcategory_name == new_subcategory_name,
                Subcategory.category_name == new_category_name,
                Subcategory.deleted_at.is_(None)
            ).first()
        )
        if not subcategory:
            return "SUBCATEGORY_NOT_FOUND"

    if "product_name" in update_data and update_data["product_name"] != product.product_name:
        existing_product = (
            db.query(Product)
            .filter(
                Product.product_name == update_data["product_name"],
                Product.product_id != product_id,
                Product.deleted_at.is_(None)
            )
            .first()
        )
        if existing_product:
            return "PRODUCT_ALREADY_EXISTS"
    # if request.product_name:
    #     product.product_name = request.product_name
    # if request.category_name:
    #     product.category_name = request.category_name
    # if request.subcategory_name:
    #     product.subcategory_name = request.subcategory_name
    # if request.product_status:
    #     product.product_status = request.product_status
    for field,value in update_data.items():
        setattr(product,field,value)
        
    db.commit()
    db.refresh(product)
    return product  