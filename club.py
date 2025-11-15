from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from decouple import config


app = FastAPI()
clubs_db = []

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY , algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"})

VALID_USERNAME = "ebin"
VALID_PASSWORD = "mysecurepass"


class Club(BaseModel):
    club_name: str
    nationality: str


@app.post("/token")
def login(username: str = Form(...), password: str = Form(...)):
    if username != VALID_USERNAME or password != VALID_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token_data = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return JSONResponse({"access_token": token, "token_type": "bearer"})


@app.get("/clubs")
def get_clubs(token_data: dict = Depends(verify_token)):
    return clubs_db

@app.get("/clubs/{club_id}")
def get_club(club_id: int,token_data: dict = Depends(verify_token)):
    global clubs_db
    return clubs_db[club_id]

@app.post("/clubs")
def create_club(club: Club,token_data: dict = Depends(verify_token)):
    global clubs_db
    clubs_db.append(club)
    return club

@app.put("/clubs/{club_id}")
def put_club(club_id: int, club:Club,token_data: dict = Depends(verify_token)):
    global clubs_db
    clubs_db[club_id] = club
    return club_id

@app.delete("/clubs/{club_id}")
def delete_club(club_id: int,token_data: dict = Depends(verify_token)):
    global clubs_db
    clubs_db.pop(club_id)
    return club_id