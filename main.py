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
# sql = "SHOW TABLES"



# Самостійна робота
# sql = "CREATE TABLE Book(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(100), author VARCHAR(50), publication_year INT, genre VARCHAR(30))"



sql = "INSERT INTO articals(title, intro, date)VALUES(%s, %s, %s)"

art = [
    ('1 стаття', ',Текст до 1 статті', '2026-03-19'),
    ('2 стаття', ',Текст до 2 статті', '2026-03-19'),
    ('3 стаття', ',Текст до 3 статті', '2026-03-18'),
    ('4 стаття', ',Текст до 4 статті', '2026-03-18'),
    ('5 стаття', ',Текст до 5 статті', '2026-03-19'),
    ('6 стаття', ',Текст до 6 статті', '2026-03-19'),
]

# sql = "DELETE FROM articals"
# # cur.execute(sql)

cur.executemany(sql, art)
db.commit()

# for el in cur:
#     print(el)

cur.close()
db.close()