from pydantic import BaseModel , Field

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
    product_name : str | None = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    category_name : str | None = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    subcategory_name : str | None = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    product_status : str | None = Field(
        default = None,
        max_length = 20
    )