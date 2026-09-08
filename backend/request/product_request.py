from pydantic import BaseModel , Field
from typing import Optional

class ProductCreateRequest(BaseModel):
    product_name: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    category_name: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    subcategory_name: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    product_status: str =Field(
        default = "Active",
        max_length = 20
    )

class ProductUpdateRequest(BaseModel):
    product_name : Optional[str] = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    category_name : Optional[str] = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    subcategory_name : Optional[str] = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    product_status : Optional[str] = Field(
        default = None,
        max_length = 20
    )