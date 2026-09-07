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
            Product.product_id == product_id
        )
        .first()
    )
    if not product:
        return None
    category_name = (
        request.category_name
        if request.category_name
        else product.category_name
    )
    subcategory_name = (
        request.subcategory_name
        if request.subcategory_name
        else request.subcategory_name
    )
    category = (
        db.query(Category)
        .filter(
            Category.category_name == category_name
        ).first()
    )
    if not category:
        return "CATEGORY_NOT_FOUND"
    subcategory = (
        db.query(Subcategory)
        .filter(
            Subcategory.subcategory_name == subcategory_name,
            Subcategory.category_name == category_name
        ).first()
    )
    if not subcategory:
        return "SUBCATEGORY_NOT_FOUND"

    if request.product_name:
        product.product_name = request.product_name
    if request.category_name:
        product.category_name = request.category_name
    if request.subcategory_name:
        product.subcategory_name = request.subcategory_name
    if request.product_status:
        product.product_status = request.product_status
    db.commit()
    db.refresh(product)
    return product  