import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="python"
)

cur = db.cursor()
# sql = "CREATE DATABASE python_learning"
# sql = "DROP DATABASE `python`"
# print((sql))


# Самостійна робота
# sql = "CREATE TABLE Books(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(100), author VARCHAR(50), publication_year INT, genre VARCHAR(30))"

# sql = "INSERT INTO art(title, intro, date)VALUES(%s, %s, %s)"
#
# arts = [
#     ('1 стаття', ',Текст до 1 статті', '2026-03-19'),
#     ('2 стаття', ',Текст до 2 статті', '2026-03-19'),
#     ('3 стаття', ',Текст до 3 статті', '2026-03-18'),
#     ('4 стаття', ',Текст до 4 статті', '2026-03-18'),
#     ('5 стаття', ',Текст до 5 статті', '2026-03-19'),
#     ('6 стаття', ',Текст до 6 статті', '2026-03-19'),
# ]

# cur.execute(sql)
sql = "SELECT title, intro FROM art WHERE intro LIKE %s OR id > %s"
cur.execute(sql, ('%2 статті%', 3))

res = cur.fetchall()
for el in res:
    print(el)

# cur.executemany(sql, arts)
# db.commit()

# for el in cur:
#     print(el)

cur.close()
db.close()