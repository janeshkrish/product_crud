from datetime import datetime
from typing import Optional
from pydantic import BaseModel , ConfigDict

class CategoryResponse(BaseModel):
    id:str
    category_id : str
    category_name : str
    category_status : str
    created_at : datetime
    updated_at : datetime
    deleted_at : Optional[datetime] = None
    model_config = ConfigDict(
        from_attributes = True
    )