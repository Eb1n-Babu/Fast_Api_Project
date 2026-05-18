import mysql.connector
from fastapi import FastAPI
from decouple import config


app = FastAPI()

product_data = mysql.connector.connect(
    host="localhost",
    user=config("USER1"),
    passwd=config("PASS1"),
    database="mobile",
    port=3306
)

if product_data.is_connected():
    print("Connected")

@app.get("/product")
def get_product():
    cursor = product_data.cursor()
    cursor.execute("select * from products")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.get("/product/{id}")
def get_product(product_id: int):
    cursor = product_data.cursor()
    cursor.execute("select * from products where id = %s",(product_id,))
    data = cursor.fetchone()
    cursor.close()
    return data