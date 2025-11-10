from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

customer_db = []

class Customer(BaseModel):
    id: int
    name: str
    email: str

@app.get("/customer")
def get_customers():
    return customer_db

@app.get("/customer/{id}")
def get_customer(id: int):
    return customer_db[id]

@app.post("/customer")
def create_customer(customer: Customer):
    customer_db.append(customer)
    return customer

@app.put("/customer/{id}")
def update_customer(customer: Customer, id: int):
    customer_db[id] = customer
    return customer

@app.delete("/customer/{id}")
def delete_customer(customer: Customer, id: int):
    customer_db.pop(id)
    return customer

