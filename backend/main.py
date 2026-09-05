import os
import shutil
from uuid import uuid4

from fastapi import(
    FastAPI,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status
)

from fastapi.middleware.cors import CORSMiddleware 
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Product
import crud

##create a database tables
Base.metadata.create_all(bind = engine)

app = FastAPI(
    title = "Product Management API",
    version = "1.0.0"
)

## cors

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173"
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


## uploads 

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok = True
)

app.mount(
    "/uploads",
    StaticFiles(directory = UPLOAD_DIR),
    name = "uploads"
)

# root 
@app.get('/')

def root():
    return {
        "message" : "Product api is running"
    }


# create product 
@app.post('/products',status_code = status.HTTP_201_CREATED)

async def create_product(
    product_id : str = Form(...),
    product_name : str = Form(...),
    product_image : UploadFile | None = File(None),
    product_price : float = Form(...),
    product_status : str = Form(...),
    db : Session = Depends(get_db)
):
    # check existing product 
    existing_product = crud.get_product(
        db,product_id
    )
    if existing_product:
        raise HTTPException(
            status_code = 400,
            detail = "Product ID already exists"
        )
    
    # save image 
    image_path = None
    if product_image:
        extension = os.path.splitext(
            product_image.filename
        )[1]
        filename = f"{uuid4()}{extension}"
        image_path = os.path.join(
            UPLOAD_DIR,
            filename
        )
        with open(
            image_path,
            "wb"
        ) as buffer:
            shutil.copyfileobj(
                product_image.file,
                buffer
            )

    # create Product 
    product = crud.create_product(
        db = db,
        product_id = product_id,
        product_name = product_name,
        product_image = image_path,
        product_price = product_price,
        product_status = product_status
    )
    return product

# get products
@app.get("/products")
def get_products(
    db:Session = Depends(get_db)
):
    return crud.get_products(db)

# get single product 
@app.get("/product/{product_id}")
def get_product(
    product_id : str,
    db:Session = Depends(get_db)
):
    product = crud.get_product(
        db,product_id
    )
    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    return product


# delete product 
@app.delete("/products/{product_id}")
def delete_product(
    product_id : str,
    db: Session = Depends(get_db)
):
    product = crud.delete_product(db,product_id)
    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        ) 
    return {
        "message" : "Product deleted Successfully"
    }