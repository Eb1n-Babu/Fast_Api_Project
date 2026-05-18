
import mysql.connector
from decouple import config
from fastapi import FastAPI


app = FastAPI(title="Mobile data")

mobiles = mysql.connector.connect(
    host="localhost",
    user=config("USER_NAME"),
    password=config("PASSWORD"),
    database=config("DATABASE_MOBILE"),
    port=3306,
)

@app.get("/")
def get_mobiles():
    cursor = mobiles.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    return data

@app.get("/{product_id}")
def get_mobile(product_id: int):
    cursor = mobiles.cursor()
    cursor.execute("SELECT * FROM products WHERE product_id=%s",(product_id,))
    data = cursor.fetchone()
    cursor.close()
    return data

@app.post("/")
def create_mobile(brand: str, model: str, description: str, price: float):
    cursor = mobiles.cursor()
    sql = "INSERT INTO products (brand, model, description, price) VALUES (%s, %s, %s, %s)"
    values = (brand, model, description, price)
    cursor.execute(sql, values)
    mobiles.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return {"message": f"Mobile {brand} was created successfully", "product_id": new_id}

@app.put("/{product_id}/update")
def update_mobile(product_id: int,brand: str, model: str, description: str, price: float):
    cursor = mobiles.cursor()
    sql = "UPDATE products SET brand=%s, model=%s, description=%s, price=%s WHERE product_id=%s"
    values = (product_id, brand, model, description, price)
    cursor.execute(sql, values)
    mobiles.commit()
    cursor.close()
    return {"message": f"Mobile {brand} was updated successfully"}

@app.patch("/{product_id}/partial_update")
def partial_update_mobile(product_id: int,brand: str, model: str, description: str, price: float):
    cursor = mobiles.cursor()
    sql = "UPDATE products SET brand=%s, model=%s, description=%s, price=%s WHERE product_id=%s"
    values = (product_id, brand, model, description, price)
    cursor.execute(sql, values)
    mobiles.commit()
    cursor.close()
    return {"message": f"Mobile {brand} was updated successfully"}

@app.delete("/{product_id}")
def delete_mobile(product_id: int):
    cursor = mobiles.cursor()
    cursor.execute("DELETE FROM products WHERE product_id=%s", (product_id,))
    mobiles.commit()
    cursor.close()
    return {"message": f"Mobile {product_id} deleted successfully"}