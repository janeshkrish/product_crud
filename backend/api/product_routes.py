from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from response.product_response import ProductResponse
from request.product_request import (ProductCreateRequest,ProductUpdateRequest)
from services.product.create_product import create_product
from services.product.delete_product import delete_product
from services.product.get_product import (get_Product,get_Products)
from services.product.update_product import update_product

router = APIRouter(
    prefix = "/product",
    tags = ["Product"]
)

@router.post(
    "",
    response_model = ProductResponse,
    status_code = status.HTTP_201_CREATED
)
def post_product(
    request : ProductCreateRequest,
    db:Session = Depends(get_db)
):
    product = create_product(
        db,
        request
    )
    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Invalid category or subcategory"
        )
    return product

@router.get(
    "",
    response_model = list[ProductResponse]
)
def get_all_product(
    db:Session = Depends(get_db)
):
    return get_Products(db)

@router.get(
    "/{product_id}"
)
def get_single_product(
    product_id  : str,
    db:Session = Depends(get_db) 
):
    product = get_Product(
        db,
        product_id
    )
    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    return product

@router.put(
        "/{product_id}",
        response_model = ProductResponse
)
def update_single_product(
    product_id:str,
    request: ProductUpdateRequest,
    db:Session = Depends(get_db)
):
    product = update_product(
        db,
        request,
        product_id
    )
    if product is None:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    if product == "CATEGORY_NOT_FOUND":
        raise HTTPException(
            status_code = 404,
            detail = "Category not found"
        )
    if product == "SUBCATEGORY_NOT_FOUND":
        raise HTTPException(
            status_code = 404,
            detail = "Subcategory not found"
        )
    return product

@router.delete(
    "/{product_id}"
)
def remove_product(
    product_id : str,
    db: Session = Depends(get_db)
):
    product = delete_product(
        db,
        product_id
    )
    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    return {
        "message" : "Product Deleted Successfully"
    }

