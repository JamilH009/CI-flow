from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Chal raha hai fastapi ka server!"}

@app.get("/obaid/")
def read_obaid():
    return {"message": "Its, obaid here ok!"}

@app.get("/jamil/")
def read_jamil():
    return {"message": "Its jamil CEO of Softbuilds!"}

class Item(BaseModel):
    id: int 
    name: str
    description: str
    
items = []

@app.post("/items/")
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item already exists")
    items.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(items):
        if item.id == item_id:
            items[idx] = updated_item
            return updated_item
        raise HTTPException(status_code=404, detail="Item not found")
    

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(items):
        if item.id == item_id:
            items.pop(idx)
            return {"message": "Item is Deleted"}
        raise HTTPException(status_code=404, detail="Item not found")
