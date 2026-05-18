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

