from django.contrib.sitemaps.views import index
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

user_db = []

class User(BaseModel):
    name: str
    age: int

@app.get("/users")
def get_users():
    return user_db

@app.get("/users/{id}")
def get_user(id: int):
    try:
        return user_db[id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: User):
    user_db.append(user)
    return user_db

@app.put("/users/{id}")
def update_user(id: int, user: User):
    try:
        user_db[id] = user
        return user_db[id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{id}")
def delete_user(id: int):
    try:
        user_db.pop(id)
        return user_db[id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")