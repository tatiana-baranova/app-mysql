import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="python-example"
)

cur = db.cursor()

# Самостійна робота
sql = "INSERT INTO book(title, author, publication_year, genre)VALUES(%s, %s, %s, %s)"
books = [
    ('The Great Gatsby','F. Scott Fitzgerald','1925','Classics'),
    ('To Kill a Mockingbird','Harper Lee','1960','Fiction'),
    ('1984','George Orwell','1949','Dystopian'),
]
cur.executemany(sql, books)
db.commit()

cur.close()
db.close()