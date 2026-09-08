from fastapi import Depends,HTTPException,status,APIRouter
from sqlalchemy.orm import Session

from database import get_db
from request.category_request import (CategoryCreateRequest,CategoryUpdateRequest)
from response.category_response import CategoryResponse
from services.category.create_category import create_category
from services.category.get_category import (get_categories,get_category)
from services.category.delete_category import delete_category
from services.category.update_category import update_category


router = APIRouter(
    prefix = "/categories",
    tags = ["Category"]
)
@router.post(
    path="",
    response_model = CategoryResponse,
    status_code = status.HTTP_201_CREATED
)
async def post_category(
    request : CategoryCreateRequest,
    db :  Session = Depends(get_db)
):
    category = create_category(db,request)
    if not category:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Category already exists"
        )
    return category

@router.get(
    "",
    response_model = list[CategoryResponse]
)
async def get_all_categories(
    db: Session = Depends(get_db)
):
    return get_categories(db)

@router.get(
    path = "/{category_id}",
    response_model = CategoryResponse
)
async def get_single_category(
    category_id : str,
    db: Session = Depends(get_db)
):
    category = get_category(
        db,
        category_id
    )
    if not category:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Category not Found"
        )
    return category

@router.put(
        "/{category_id}",
        response_model = CategoryResponse
)
async def update_single_category(
    category_id : str,
    request : CategoryUpdateRequest,
    db : Session = Depends(get_db)
):
    category = update_category(
        db,
        category_id,
        request
    )
    if category is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Category not found"
        )
    if category == "CATEGORY_ALREADY_EXIT":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Category already exist"
        )
    return category

@router.delete(
    "/{category_id}"
)
async def remove_category(
    category_id : str,
    db : Session = Depends(get_db)
):
    category = delete_category(
        db,
        category_id
    )
    if category is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Category not Found"
        )
    if category == "CATEGORY_IN_USE":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Category cannot be deleted because it is been used"
        )
    return {
        "message" : "Category has been sucessfully deleted" 
    }

