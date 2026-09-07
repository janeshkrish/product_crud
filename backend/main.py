from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from models.category_model import Category
from models.subcategory_model import Subcategory
from models.product_model import Product
from api.category_routes import router as category_router
from api.product_routes import router as product_router
from api.subcategory_routes import router as subcategory_router

Base.metadata.create_all(bind = engine)

app = FastAPI(
    title = "Product management System",
    version = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173"
    ],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router)
app.include_router(subcategory_router)
app.include_router(product_router)

@app.get("/")
def root():
    return{
        "message" : "Product api is running"
    }