import mysql.connector
from fastapi import FastAPI
from decouple import config

app = FastAPI()

school_data = mysql.connector.connect(
    host="localhost",
    user=config("USER1"),
    passwd=config("PASS1"),
    database="school",
    port="3306"
)

if school_data.is_connected():
    print("Connected to database")


@app.get("/student/")
def students():
    cursor = school_data.cursor()
    cursor.execute("select * from students")
    data = cursor.fetchall()
    return data

@app.get("/student/{student_id}/")
def student(student_id: int):
    cursor = school_data.cursor()
    cursor.execute("select * from students where student_id = %s",(student_id,))
    data = cursor.fetchone()
    return data
