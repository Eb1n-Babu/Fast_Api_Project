import mysql.connector
from fastapi import FastAPI
from decouple import config


app = FastAPI()

student = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config("PASSWORD"),
    database=config("DATABASE")
)

@app.get("/students/")
def get_students():
    cursor = student.cursor()
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    return students

@app.get("/student/{name}")
def get_student(name: str):
    cursor = student.cursor()
    cursor.execute("SELECT * FROM student WHERE name = %s",(name,))
    students = cursor.fetchone()
    return students

@app.post("/students/")
def post_student(name,age,location):
    cursor = student.cursor()
    cursor.execute("insert into students values(%s,%s,%s)",(name,age,location))
    student.commit()
    return {"message":"Student added successfully"}




