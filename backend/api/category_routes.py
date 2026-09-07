from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy import Session

from database import get_db
from request.category_request import (CategoryCreateRequest,CategoryUpdateRequest)
from response.category_response import CategoryResponse
from services.category.create_category import create_category
from services.category.get_category import (get_categories,get_category)
from services.category.delete_category import delete_category


router = APIRouter(
    prefix = "/category",
    tag = ["Category"]
)
@router.post(
    path="",
    response_model = CategoryResponse,
    status_code = status.HTTP_201_CREATED
)
def post_category(
    request = CategoryCreateRequest,
    db :  Session = Depends(get_db)
):
    category = create_category(db,request)
    if not category:
        raise HTTPException(
            status_code = 404,
            detail = "Category already exists"
        )
    return category

