import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S@2002#",
    database="employee_db"
)

cursor = conn.cursor()