# schemas.py or models.py
from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    quantity: int