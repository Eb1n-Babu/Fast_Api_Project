from mysql import connector

champions_league = connector.connect(
    host="localhost",
    user="root",
    password="@Ebinbabu2209",
    database="uefa_champions_league",
)

if champions_league.is_connected():
    print(champions_league.is_connected())

cursor = champions_league.cursor()
cursor.execute("SELECT * FROM teams")
rows = cursor.fetchall()
print(rows)