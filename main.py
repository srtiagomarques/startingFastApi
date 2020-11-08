from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    """
    Leitura root. Hello World da minha primeria API. 
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Busca um determinado item pelo seu id.
    """
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Realiza atualização de registro de item.
    """
    return {"item_name": item.name, "item_id": item_id}