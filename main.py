from fastapi import FastAPI
from models import Product

app= FastAPI()
@app.get("/")
def greet():
    return "I love you!!!"

products=[
    Product(id=1,name="Laptop",description="This is a laptop",price=1000.0,quantity=10),
    Product(id=2,name="Mobile",description="This is a mobile",price=500.0,quantity=20),
    Product(id=3,name="Tablet",description="This is a tablet",price=300.0,quantity=15),
    Product(id=4,name="Headphones",description="This is a headphones",price=100.0,quantity=30),
    Product(id=5,name="Smartwatch",description="This is a smartwatch",price=200.0,quantity=25)
]

@app.get("/product")
def all_product():
    return products
@app.get("/product/{id}")
def get_product(id: int):
    return products[id-1]
