from fastapi import FastAPI

app= FastAPI()
@app.get("/")
def greet():
    return "I love you!!!"

@app.get("/product")
def all_product():
    return "All products"