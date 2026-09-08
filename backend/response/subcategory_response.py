from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class SubcategoryResponse(BaseModel):
    id : str
    subcategory_id : str
    subcategory_name : str
    category_name : str
    subcategory_status : str
    created_at : datetime
    updated_at : datetime
    deleted_at : Optional[datetime] = None
    model_config = ConfigDict(
        from_attributes = True
    )
