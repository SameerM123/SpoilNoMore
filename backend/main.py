from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI()

# garbage database example for now
inventory = []


class FoodItem(BaseModel):  #we can add more stuff like type of food (fruit, meat), or whatever later
    name: str
    expiry_date: date

@app.get("/items", response_model=List[FoodItem])
def get_items():
    return inventory

@app.post("/items")
def add_item(item: FoodItem):
    inventory.append(item)
    return {"message": "Item added", "item": item}

@app.delete("/items/{item_index}")
def delete_item(item_index: int):
    if 0 <= item_index < len(inventory):
        removed = inventory.pop(item_index)
        return {"message": "Item removed", "item": removed}
    return {"error": "Item not found"}
