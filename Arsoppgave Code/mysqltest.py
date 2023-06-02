import mysql.connector

mydb = mysql.connector.connect(
    host="10.2.2.198",
    user="root",
    password="Root4l1fe",
    database="Highscores"
)
print(mydb)

