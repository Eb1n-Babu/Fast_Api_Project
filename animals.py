from fastapi import FastAPI
from pydantic import BaseModel

import animal

app = FastAPI()

animals_data = []

class Animals(BaseModel):
    animal_id: int
    animal_name: str
    animal_place: str

@app.post("/animals")
def create_animals(animals:Animals):
    animals_data.append(animals)
    return f"animals created!"

@app.get("/animals")
def get_animals():
    return animals_data



