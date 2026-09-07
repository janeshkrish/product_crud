from pydantic import BaseModel , ConfigDict

class CategoryResponse(BaseModel):
    category_id : str
    category_name : str
    category_status : str
    model_config = ConfigDict(
        from_attributes = True
    )