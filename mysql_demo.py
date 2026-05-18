from fastapi import FastAPI
from decouple import config
import mysql.connector

app = FastAPI()

connection  = mysql.connector.connect(
    host="localhost",
    user= config("USER_NAME"),
    password= config("PASSWORD"),
    database=config("DATABASE_PATIENT_RECORDS"),
)

print(connection.is_connected)

@app.get("/")
def get_students():
    cursor = connection.cursor()
    cursor.execute("select * from patient_records")
    students = cursor.fetchall()
    cursor.close()
    return students

@app.get("/{name}")
def get_students(name: str):
    cursor = connection.cursor()
    cursor.execute("select * from patient_records where name = %s",(name,))
    students = cursor.fetchall()
    cursor.close()
    return students

@app.post("/")
def create_student(name,age,location):
    cursor = connection.cursor()
    cursor.execute("insert into patient_records values(%s,%s,%s)", (name, age, location))
    connection.commit()
    return {"message": "Student added successfully"}



