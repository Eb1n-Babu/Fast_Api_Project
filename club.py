from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="club API")

club_data_base = []

class Club(BaseModel):
    name: str
    count: int

@app.get("clubs/")
def get_clubs():
    return club_data_base

@app.post("/clubs/")
def create_club(club:Club):
    club_data_base.append(club)
    return club_data_base

@app.get("/club/{club_id}")
def get_club(club_id:int):
    try:
        global club_data_base
        return club_data_base[club_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="club not found")

@app.put("/club/{club_id}")
def update_club(club_id:int, club:Club):
    try:
        global club_data_base
        club_data_base[club_id] = club
        return club_data_base[club_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="club not found")

@app.delete("/club/{club_id}")
def delete_club(club_id:int):
    try:
        global club_data_base
        club_data_base.pop(club_id)
    except IndexError:
        raise HTTPException(status_code=404, detail="club not found")




