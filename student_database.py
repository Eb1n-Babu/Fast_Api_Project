# app.py  →  Super Simple FastAPI + MySQL (India 2025)
from fastapi import FastAPI
import pymysql
from decouple import config

app = FastAPI(title="Data base")

conn = pymysql.connect(
    host="localhost",
    user= config("user1"),
    password= config("pass1"),
    database=config("mydb1"),
    charset="utf8mb4"
)

@app.post("/student")
def student(name:str , age:int , location:str):
    cursor = conn.cursor()
    cursor.execute("insert into student(name,age,location) values (%s,%s,%s)",args=[name,age,location])
    conn.commit()
    return {"status": "Student added!"}

@app.get("/student")
def get_student():
    cursor = conn.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    cursor.close()
    return {"students": rows}

@app.get("/student/{name}")
def get_student(name: str):
    cursor = conn.cursor()
    cursor.execute("select * from student where name = %s",args=[name])
    rows = cursor.fetchall()
    cursor.close()
    return {"students": rows}



