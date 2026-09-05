from sqlalchemy.orm import Session
from models import Product


## Create 
def create_product(
    db : Session,
    product_id : str,
    product_name : str,
    product_image : str | None,
    product_price : float,
    product_status : str
): 
    product = Product(
        product_id = product_id,
        product_name = product_name,
        product_image = product_image,
        product_price = product_price,
        product_status = product_status
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

## read all products
def get_products(db:Session):
    return db.query(Product).all()


## read 1 product
def get_product(db:Session,product_id:str):
    return db.query(Product).filter(
        Product.product_id == product_id
    ).first()


#delete
def delete_product(db:Session,product_id:str):
    product = get_product(db,product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product

