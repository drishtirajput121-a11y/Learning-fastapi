from fastapi import FastAPI
from models import Product

app= FastAPI()
@app.get("/")
def greet():
    return "I love you!!!"

products=[
    Product(1,"Laptop","This is a laptop",1000.0,10),
    Product(2,"Mobile","This is a mobile",500.0,20),
    Product(3,"Tablet","This is a tablet",300.0,15),
    Product(4,"Headphones","This is a headphones",100.0,30),
    Product(5,"Smartwatch","This is a smartwatch",200.0,25)
]

@app.get("/product")
def all_product():
    return products

