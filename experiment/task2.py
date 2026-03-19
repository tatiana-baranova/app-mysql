import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="my-data"
)

cur = db.cursor()


sql = "CREATE DATABASE `my-data`"
cur.execute(sql)

# db.commit()


cur.close()
db.close()