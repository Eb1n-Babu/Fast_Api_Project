from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

animal_db = []

class Animals(BaseModel):
    animal_id: int
    animal_name: str


@app.get("/animals/")
def get_animals():
    return animal_db

@app.get("/animals/{animal_id}")
def get_animal(animal_id: int):
    global animal_db
    return animal_db[animal_id]

@app.post("/animals")
def create_animal(animal: Animals):
    animal_db.append(animal)
    return animal

@app.put("/animals/{animal_id}")
def update_animal(animal_id: int, new_animal: Animals):
    global animal_db
    animal_db[animal_id] = new_animal
    return new_animal

@app.delete("/animals/{animal_id}")
def delete_animal(animal_id: int):
    global animal_db
    animal_db.pop(animal_id)
    return animal_db