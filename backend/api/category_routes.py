from fastapi import Depends,HTTPException,status,APIRouter
from sqlalchemy.orm import Session

from database import get_db
from request.category_request import (CategoryCreateRequest,CategoryUpdateRequest)
from response.category_response import CategoryResponse
from services.category.create_category import create_category
from services.category.get_category import (get_categories,get_category)
from services.category.delete_category import delete_category


router = APIRouter(
    prefix = "/category",
    tags = ["Category"]
)
@router.post(
    path="",
    response_model = CategoryResponse,
    status_code = status.HTTP_201_CREATED
)
def post_category(
    request : CategoryCreateRequest,
    db :  Session = Depends(get_db)
):
    category = create_category(db,request)
    if not category:
        raise HTTPException(
            status_code = 404,
            detail = "Category already exists"
        )
    return category

@router.get(
    path = "",
    response_model = list[CategoryResponse]
)
def get_all_categories(
    db: Session = Depends(get_db)
):
    return get_categories(db)

@router.get(
    path = "/{category_id}",
    response_model = CategoryResponse
)
def get_single_category(
    category_id : str,
    db: Session = Depends(get_db)
):
    category = get_category(
        db,
        category_id
    )
    if not category:
        raise HTTPException(
            status_code = 404,
            detail = "Category not Found"
        )
    return category

@router.delete(
    path = "/{category_id}"
)
def remove_category(
    category_id : str,
    db : Session = Depends(get_db)
):
    category = delete_category(
        db,
        category_id
    )
    if category is None:
        raise HTTPException(
            status_code = 404,
            detail = "Category not Found"
        )
    if category == "CATEGORY_IN_USE":
        raise HTTPException(
            status_code = 400,
            detail = "Category cannot be deleted because it is been used"
        )
    return {
        "message" : "Category been deleted" 
    }

