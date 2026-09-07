from pydantic import BaseModel, ConfigDict

class ProductResponse(BaseModel):
    product_id : str
    product_name : str
    category_id : str
    subcategory_id : str
    product_status : str
    model_config = ConfigDict(
        from_attributes = True
    )