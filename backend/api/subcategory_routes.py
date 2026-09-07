from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from request.subcategory_request import (SubcategoryCreateRequest,SubcategoryUpdateRequest)
from response.subcategory_response import SubcategoryResponse
from services.subcategory.create_subcategory import create_subcategory
from services.subcategory.get_subcategory import (get_subcategoris,get_subcategory)
from services.subcategory.delete_subcategory import delete_subcategory

router = APIRouter(
    prefix = "/subcategories",
    tags = ["Subcategories"]
)

@router.post(
    "",
    response_model = SubcategoryResponse,
    status_code = status.HTTP_201_CREATED
)
def post_subcategory(
    request : SubcategoryCreateRequest,
    db: Session = Depends(get_db)
):
    subcategory = create_subcategory(
        db,
        request
    )
    if not subcategory:
        raise HTTPException(
            status = 404,
            detail = "Subcategory not found or Subcategory already exists"
        )
    return subcategory

@router.get(
    "",
    response_model = list[SubcategoryResponse],
)
def get_all_subcategories(
    db : Session = Depends(get_db)
):
    return get_subcategoris(db)

@router.get(
    "/{subcategory_id}",
    response_model = SubcategoryResponse
)
def get_single_subcategory(
    subcategory_id : str,
    db : Session = Depends(get_db)
):
    subcategory = get_subcategory(
        db,
        subcategory_id
    )
    if not subcategory:
        raise HTTPException(
            status_code = 404,
            detail = "Category not found"
        )
    return subcategory

@router.delete(
    "/{subcategory_id}"
)
def remove_subcategory(
    subcategory_id : str,
    db: Session = Depends(get_db)
):
    subcategory = delete_subcategory(
        db,
        subcategory_id
    )
    if not subcategory:
        raise HTTPException(
            status_code = 400,
            detail = "SubCategory cannot be deleted because it is being used"
        )
    return {
        "message" : "SubCategory deleted successfully"
    }