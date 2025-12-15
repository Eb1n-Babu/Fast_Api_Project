import decimal

import mysql.connector
from decouple import config
from fastapi import FastAPI


app = FastAPI(title="Mobile data")

mobiles = mysql.connector.connect(
    host=config("MYSQL_HOST"),
    user=config("MYSQL_USER_NAME"),
    password=config("PASSWORD"),
    database=config("MYSQL_DATABASE_NAME"),
    port=config("MYSQL_PORT"),
)

@app.get("/mobiles/")
def get_mobiles():
    cursor = mobiles.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    return data

@app.get("/mobiles/{mobile_id}")
def get_mobile(mobile_id: int):
    cursor = mobiles.cursor()
    cursor.execute("SELECT * FROM products WHERE id=%s",(mobile_id,))
    data = cursor.fetchone()
    return data

@app.post("/mobiles/{mobile_id}/update")
def update_mobile(mobile_id: int ,brand:str,model:str,description:str,mobile_price:int):
    cursor = mobiles.cursor()
    cursor.execute("Update products set price=%s where id=%s",(mobile_id,brand,model,description,mobile_price))
    mobiles.commit()
    return f"Mobile {mobile_id} was updated successfully"

@app.post("/mobiles/")
def create_mobile(brand:str,model:str,description:str,mobile_price:int):
    cursor = mobiles.cursor()
    cursor.execute("insert into products(brand,model,description,price) values (%s,%s,%s,%s)",(brand,model,description,mobile_price))
    mobiles.commit()
    return f"Mobile {brand} was created successfully"

@app.delete("/mobiles/{mobile_id}")
def delete_mobile(mobile_id: int):
    cursor = mobiles.cursor()
    cursor.execute("delete from products where id=%s",(mobile_id,))
    mobiles.commit()
    return f"Mobile {mobile_id} was deleted successfully"
