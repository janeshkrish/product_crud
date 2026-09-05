from pydantic import BaseModel,ConfigDict

class Productresponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)   
    product_id : str 
    product_name : str 
    product_image : str | None
    product_price : float 
    product_status : str 
