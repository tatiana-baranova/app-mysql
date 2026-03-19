import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="python"
)
cur = db.cursor()

sql = "CREATE TABLE Statistic(name VARCHAR(50), age INT(3), city VARCHAR(50))"
cur.execute(sql)


# cur.executemany(sql, arts)
# db.commit()

cur.close()
db.close()

# sql = "SHOW TABLES"
# print((sql))
# sql = "DROP DATABASE `python`"