from fastapi import FastAPI
from decouple import config
import mysql.connector

app = FastAPI(title="Employee API")

employee_db = mysql.connector.connect(
    host="localhost",
    user=config("USER_NAME"),
    passwd=config("PASSWORD"),
    database=config("DATABASE"),
    port="3306",
)

if employee_db.is_connected():
    print("Connected")

@app.get("/")
def get_employees():
    cursor = employee_db.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.get("/{employee_id}")
def get_employee(employee_id: int):
    cursor = employee_db.cursor()
    cursor.execute("SELECT * FROM employee WHERE employee_id = %s",(employee_id,))
    data = cursor.fetchone()
    cursor.close()
    return data

@app.post("/")
def post_employees(employee_id:int,first_name: str,last_name: str,email: str,department: str,salary : int,hire_date:
    int,country: str,phone : int ,status: str="Active"):
    cursor = employee_db.cursor()
    cursor.execute("INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (employee_id,first_name,last_name,email,department,salary,hire_date,country,phone,status))

    cursor.close()
    return f"successfully added employee"


@app.delete("/{employee_id}")
def delete_employee(employee_id:int):
    cursor = employee_db.cursor()
    cursor.execute("DELETE FROM employee WHERE employee_id = %s", (employee_id,))
    cursor.close()
    return f"successfully deleted the  employee"