from pydantic import BaseModel , Field
from typing import Optional

class SubcategoryCreateRequest(BaseModel):
    subcategory_name: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    category_name: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    subcategory_status: str = Field(
        default = "Active",
        max_length = 20
    )

class SubcategoryUpdateRequest(BaseModel):
    subcategory_name : Optional[str] = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    category_name : Optional[str] = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    subcategory_status : Optional[str] = Field(
        default = None,
        max_length = 20
    )