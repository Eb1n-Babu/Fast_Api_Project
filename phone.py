from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="phone")

phone_data_base = []

class Phone(BaseModel):
    name: str
    year: str

@app.get("/phones")
def get_phones():
    return phone_data_base

@app.post("/phones")
def create_phone(phone: Phone):
    phone_data_base.append(phone)
    return phone_data_base

@app.get("/phones/{phone_id}")
def get_phone(phone_id: int):
    global phone_data_base
    return phone_data_base[phone_id]

@app.put("/phones/{phone_id}")
def update_phone(phone_id: int, phone: Phone):
    global phone_data_base
    phone_data_base[phone_id] = phone
    return phone_data_base

@app.delete("/phones/{phone_id}")
def delete_phone(phone_id: int):
    global phone_data_base
    phone_data_base.pop(phone_id)
    return phone_data_base
