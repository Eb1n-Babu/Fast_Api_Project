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

@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    global customer_db
    return customer_db[customer_id]

@app.post("/customer")
def create_customer(customer: Customer):
    customer_db.append(customer)
    return customer

@app.put("/customer/{id}")
def update_customer(customer: Customer,customer_id : int):
    global customer_db
    customer_db[customer_id] = customer
    return customer

@app.delete("/customer/{id}")
def delete_customer(customer_id: int):
    customer_db.pop(customer_id)
    return Customer

