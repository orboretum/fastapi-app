from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI app instance
app = FastAPI()

# Define a data model for validation
class Item(BaseModel):
    name: str
    description: str
    price: float

# Root endpoint
@app.get("/")
async def home():
    return {"message": "Welcome to my FastAPI service!"}

# Endpoint to fetch data
@app.get("/data")
async def get_data():
    return {"status": "success", "data": {"title": "FastAPI + Webflow"}}

# Endpoint to accept user input via POST request
@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item '{item.name}' added successfully!", "data": item}