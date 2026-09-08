from sqlalchemy.orm import Session
from models.category_model import Category
from models.subcategory_model import Subcategory
from models.product_model import Product
from request.product_request import ProductCreateRequest

def create_product(
        db: Session,
        request : ProductCreateRequest
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
    subcategory = (
        db.query(Subcategory)
          .filter(
            Subcategory.subcategory_name == request.subcategory_name,  
            Subcategory.category_name == request.category_name,
            Subcategory.deleted_at.is_(None)
        )
        .first()
    )
    if not subcategory:
        return "SUBCATEGORY_NOT_FOUND"
    existing_product = (
        db.query(Product)
        .filter(
            Product.product_name == request.product_name,
            Product.deleted_at.is_(None)    
        )
        .first()
    )
    if existing_product:
        return "PRODUCT_ALREADY_EXISITS"
    last_product = (
        db.query(Product)
        .order_by(Product.product_id.desc())
        .wait_for_update()
        .first()
    )
    if last_product:
        last_number = int(
            last_product.product_id.split("-")[1]
        )
        next_number = last_number + 1
    else:
        next_number = 1
    product_id = f"P-{next_number:02d}"
    product = Product(
        product_id = product_id,
        product_name = request.product_name,
        category_name = request.category_name,
        subcategory_name = request.subcategory_name,
        product_status = request.product_status
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product