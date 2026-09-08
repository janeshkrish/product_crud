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
    prefix = "/products",
    tags = ["Product"]
)

@router.post(
    "",
    response_model = ProductResponse,
    status_code = status.HTTP_201_CREATED
)
async def post_product(
    request : ProductCreateRequest,
    db:Session = Depends(get_db)
):
    product = create_product(
        db,
        request
    )
    if product == "CATEGORY_NOT_FOUND":
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "The specified parent category does not exist or is inactive"
        )
    if product == "SUBCATEGORY_NOT_FOUND":
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "The specified subcategory does not exist under this category"
        )
    if product == "PRODUCT_ALREADY_EXISITS":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "A product with this name already exist"
        )
    # if not product:
    #     raise HTTPException(
    #         status_code = 404,
    #         detail = "Invalid category or subcategory"
    #     )
    return product

@router.get(
    "",
    response_model = list[ProductResponse]
)
async def get_all_product(
    db:Session = Depends(get_db)
):
    return get_Products(db)

@router.get(
    "/{product_id}"
)
async def get_single_product(
    product_id  : str,
    db:Session = Depends(get_db) 
):
    product = get_Product(
        db,
        product_id
    )
    if not product:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Product not found"
        )
    return product

@router.put(
        "/{product_id}",
        response_model = ProductResponse
)
async def update_single_product(
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
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Product not found"
        )
    if product == "CATEGORY_NOT_FOUND":
        raise HTTPException(
            status_code = status.HTTP_442_UNPROCESSABLE_ENTITY,
            detail = "Target category name does not exist or has been disabled"
        )
    if product == "SUBCATEGORY_NOT_FOUND":
        raise HTTPException(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail = "Target subcategory name does not map to this specific category choice"
        )
    if product == "PRODUCT_ALREADY_EXISTS":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Product name already taken by another item in stock"
        )
    return product

@router.delete(
    "/{product_id}"
)
async def remove_product(
    product_id : str,
    db: Session = Depends(get_db)
):
    product = delete_product(
        db,
        product_id
    )
    if not product:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Product not found or already removed"
        )
    return {
        "message" : "Product Deleted Successfully"
    }

