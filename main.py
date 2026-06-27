from fastapi import FastAPI
from database import session, engine
from database_models import Base, Product
from schemas import ProductSchema       
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "I love you!!!"}

@app.get("/product")
def all_product():
    return session.query(Product).all()

@app.get("/product/{id}")
def get_product(id: int):
    product = session.query(Product).filter(Product.id == id).first()
    if product:
        return product
    return {"message": "Product not found"}

@app.post("/product")
def add_product(data: ProductSchema):   
    product = Product(
        name=data.name,
        description=data.description,
        price=data.price,
        quantity=data.quantity
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@app.put("/product/{id}")
def update_product(id: int, data: ProductSchema):
    product = session.query(Product).filter(Product.id == id).first()
    if not product:
        return {"message": "Product not found"}
    product.name = data.name
    product.description = data.description
    product.price = data.price
    product.quantity = data.quantity
    session.commit()
    return product

@app.delete("/product/{id}")
def delete_product(id: int):
    product = session.query(Product).filter(Product.id == id).first()
    if not product:
        return {"message": "Product not found"}
    session.delete(product)
    session.commit()
    return {"message": "Deleted Successfully"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)