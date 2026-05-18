import mysql.connector
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Champions League")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Ebinbabu2209",
    database="uefa_champions_league",
    port=3306,
)

if mydb.is_connected():
    print("Connected to MySQL")

@app.get("/teams/")
def read_teams():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    return teams

@app.get("/teams/{team_id}")
def read_team(team_id: int):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM teams WHERE team_id = %s", (team_id,))
    team = cursor.fetchone()
    return team

if __name__ == "__main__":
    uvicorn.run("champions_league:app", host="127.0.0.1", port=8000, reload=True)
