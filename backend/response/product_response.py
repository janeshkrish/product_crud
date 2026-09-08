from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProductResponse(BaseModel):
    id : str
    product_id : str
    product_name : str
    category_name : str
    subcategory_name : str
    product_status : str
    created_at : datetime
    updated_at : datetime
    deleted_at : Optional[datetime] = None
    model_config = ConfigDict(
        from_attributes = True
    )