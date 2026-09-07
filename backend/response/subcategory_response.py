from pydantic import BaseModel, ConfigDict

class SubcategoryResponse(BaseModel):
    subcategory_id : str
    subcategory_name : str
    category_name : str
    subcategory_status : str
    model_config = ConfigDict(
        from_attributes = True
    )
