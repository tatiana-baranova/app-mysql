import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="python-example"
)

cur = db.cursor()

# sql = "CREATE DATABASE `python-example`"
# sql = "DROP DATABASE `python`"
# sql = "SHOW DATABASES"
# sql = "CREATE TABLE users(name VARCHAR(50), age INT(3))"
sql = "SHOW TABLES"
cur.execute(sql)

for el in cur:
    print(el)

cur.close()
db.close()