to check connection : 
python -i models.py 
from database import engine
Base.metadata.create_all(bind=engine)
test = Product(product_id="P101",product_name="mouse",product_price=29.99)
test.product_id


python3 -m venv venv
source venv/bin/activate
uvicorn main:app --reload