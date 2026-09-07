from pydantic import BaseModel , Field

class CategoryCreateRequest(BaseModel):
    category_name: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    category_status: str = Field(
        default = "Active",
        max_length = 20
    )

class CategoryUpdateRequest(BaseModel):
    category_name : str | None = Field(
        default = None,
        min_length = 1,
        max_length = 100
    )
    category_status : str | None = Field(
        default = None,
        max_length = 20
    )