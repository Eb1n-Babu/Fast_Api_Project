# app.py  →  Super Simple FastAPI + MySQL (India 2025)
from fastapi import FastAPI
import pymysql
from decouple import config

app = FastAPI(title="My First API")


conn = pymysql.connect(
    host="localhost",
    user= config("user"),
    password= config("pass"),
    database=config("mydb"),
    charset="utf8mb4"
)

@app.get("/")
def home():
    return {"message": "Namaste! Your API is LIVE"}

@app.post("/add")
def add(name: str, email: str):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    return {"status": "Added!", "name": name, "email": email}

@app.get("/users")
def all_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    users = [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]
    return {"total": len(users), "users": users}