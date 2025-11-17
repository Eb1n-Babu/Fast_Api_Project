from fastapi import FastAPI
import mysql.connector
from decouple import config

emp = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config('MYSQL_USER'),
    port=3306,
    database=config('MYSQL_DATABASE')
)

app = FastAPI(title="employee")

@app.get("/employees/")
def get_employee():
    cursor = emp.cursor()
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    emp.close()
    return data
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    cursor = emp.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = %s",(emp_id,))
    data = cursor.fetchone()
    emp.close()
    return data
@app.post("/employees/")
def create_employee(first_name, last_name, email, department, salary, hire_date, country, phone, status):
    cursor = emp.cursor()
    cursor.execute("INSERT INTO employees(first_name, last_name, email, department, salary, hire_date, country, phone, status)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(first_name, last_name, email, department, salary, hire_date, country, phone, status))
    emp.commit()
