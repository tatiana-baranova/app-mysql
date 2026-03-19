import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="python"
)

cur = db.cursor()

# Самостійна робота
# sql = "INSERT INTO Books(title, author, publication_year, genre)VALUES(%s, %s, %s, %s)"
# books = [
#     ('The Great Gatsby','F. Scott Fitzgerald','1925','Classics'),
#     ('To Kill a Mockingbird','Harper Lee','1960','Fiction'),
#     ('1984','George Orwell','1949','Dystopian'),
# ]
# cur.executemany(sql, books)
# sql = "SELECT title, genre FROM Books WHERE genre <> 'Fiction'"
sql = "SELECT title, genre FROM Books WHERE genre = 'Fiction'"
cur.execute(sql)

res = cur.fetchall()
for el in res:
    print(el)

# db.commit()


cur.close()
db.close()