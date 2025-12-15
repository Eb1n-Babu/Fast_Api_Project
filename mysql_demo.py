from fastapi import FastAPI
from decouple import config
import mysql.connector

app = FastAPI()

connection  = mysql.connector.connect(
host="localhost",
    user= config("user"),
    password= config("pass"),
    database=config("mydb"),
)

print(connection.is_connected)

@app.get("/students/")
def get_students():
    cursor = connection.cursor()
    cursor.execute("select * from student")
    students = cursor.fetchall()
    cursor.close()
    return students

@app.get("/student/{name")
def get_students(name: str):
    cursor = connection.cursor()
    cursor.execute("select * from student where name = %s",(name,))
    students = cursor.fetchall()
    cursor.close()
    return students

@app.post("/students/")
def create_student(name,age,location):
    cursor = connection.cursor()
    cursor.execute("insert into student values(%s,%s,%s)", (name, age, location))
    connection.commit()
    return {"message": "Student added successfully"}



