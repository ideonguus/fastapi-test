"""
This is the main file for the FastAPI application.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    Test route for base URL.
    """
    return {"message": "Hello, FastAPI!"}

@app.get("/users/{user_id}")
async def read_item(user_id: int):
    """
    Test route for /items/{item_id}.
    """
    return {"user_id": user_id}
