from fastapi import FastAPI
from pydantic import BaseModel

from main import Book

app = FastAPI(title="FastAPI")

db_student = []

class Student(BaseModel):
    name: str
    age: int

@app.get("/students")
def get_students():
    return db_student

@app.get("students/{student_id}")
def get_student(student_id: int):
    return db_student[student_id]

@app.post("/students")
def create_student(student: Student):
    db_student.append(student)
    return student

@app.put("/students/{student_id}")
def update_student(student: Student, student_id: int):
    db_student[student_id] = student
    return student

@app.delete("/students/{student_id}")
def delete_student(student: Student , student_id: int):
    db_student.pop(student_id)
    return student

