from fastapi import FastAPI
import mysql.connector

app = FastAPI()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Ebinbabu2209",
    database="userprofile",
    port="3306",
)

@app.get("/users/")
def get_users():
    cursor = connection.cursor()
    cursor.execute("select * from userlist")
    users = cursor.fetchall()
    cursor.close()
    return users

@app.get("/users/{user_id}/")
def get_user(user_id: int):
    cursor = connection.cursor()
    cursor.execute("select * from userlist where id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user
@app.post("/users/")
def update_user(id:int,name: str,email: str,age: int,city: str):
    cursor = connection.cursor()
    cursor.execute("insert into userlist values(%s,%s,%s,%s,%s)",(id,name,email,age,city))
    connection.commit()
    cursor.close()


