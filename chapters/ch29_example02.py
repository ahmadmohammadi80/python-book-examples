# Python book chapter 29, example 2
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ItemIn(BaseModel):
    name: str
    price: int = Field(ge=0)

@app.post("/items")
def create_item(item: ItemIn):
    return {"id": 1, "name": item.name, "price": item.price}
