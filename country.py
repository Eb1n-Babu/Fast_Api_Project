from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

country_data_base = []

class Country(BaseModel):
    name: str
    year: int

@app.get("/country")
def get_country():
    return country_data_base

@app.post("/country")
def post_country(country: Country):
    try:
        global country_data_base
        country_data_base.append(country)
        return country_data_base
    except IndexError:
        raise HTTPException(status_code=404, detail="Country not found")
@app.get("/country/{club_id}")
def get_country(club_id: int):
    try:
        global country_data_base
        country_data_base.append(club_id)
        return country_data_base
    except IndexError:
        raise HTTPException(status_code=404, detail="Country not found")
@app.put("/country/{club_id}")
def put_country(club_id: int, country: Country):
    try:
        global country_data_base
        country_data_base.append(club_id)
        return country_data_base
    except IndexError:
        raise HTTPException(status_code=404, detail="Country not found")
@app.delete("/country/{club_id}")
def delete_country(club_id: int):
    try:
        global country_data_base
        country_data_base.append(club_id)
        return country_data_base
    except IndexError:
        raise HTTPException(status_code=404, detail="Country not found")