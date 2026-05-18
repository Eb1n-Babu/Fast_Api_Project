import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPITutorial")

class  Student(BaseModel):
    name: str
    age: int
    score: float

student = []

@app.get("/")
def get_students():
    return student

@app.get("/{student_id}")
def get_student(student_id: int):
    return student[student_id]

@app.post("/")
def create_student(student_data: Student):
    student.append(student_data)
    return "Student created"

@app.put("/{student_id}")
def update_student(student_id: int, student_data: Student):
    student[student_id] = student_data
    return "Student updated"

@app.delete("/{student_id}")
def delete_student(student_id: int):
    del student[student_id]
    return "Student deleted"

