from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="club API")

club_db = []

class club(BaseModel):
    title: str
    author: str

@app.get("/club")
def club_list():
    return club_db

@app.post("/club")
def club_create(club: club):
    club_db.append(club)
    return club

@app.get("/club/{club_id}")
def club_get(club_id: int):
    try:
        return club_db[club_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="club not found")

