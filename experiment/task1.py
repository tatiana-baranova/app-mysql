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
#     # ('The Great Gatsby','F. Scott Fitzgerald','1925','Classics'),
#     # ('To Kill a Mockingbird','Harper Lee','1960','Fiction'),
#     # ('1984','George Orwell','1949','Dystopian'),
#     # ('The Great Gatsby','F. Scott Fitzgerald','1925','Classics'),
#     # ('To Kill a Mockingbird','Harper Lee','1960','Fiction'),
#     # ('1984','George Orwell','1949','Dystopian'),
#     # ('Pride and Prejudice','Jane Austen','1813','Romance'),
#     # ('The Catcher in the Rye','J.D. Salinger','1951','Fiction'),
#     # ('The Hobbit','J.R.R. Tolkien','1937','Fantasy'),
#     # ('Moby-Dick','Herman Melville','1851','Adventure'),
#     # ('War and Peace','Leo Tolstoy','1869','Historical'),
#     # ('The Odyssey','Homer','-800','Epic'),
#     # ('Brave New World','Aldous Huxley','1932','Dystopian')
# ]
# cur.executemany(sql, books)
# sql = "SELECT title, genre FROM Books WHERE genre <> 'Fiction'"
# sql = "SELECT title, author, publication_year FROM Books WHERE publication_year > '1950' ORDER BY publication_year DESC"
# cur.execute(sql)
#
# res = cur.fetchall()
# for el in res:
#     print(el)

# sql = "UPDATE Books SET publication_year = '1950' WHERE title = '1984'"
sql = "DELETE FROM Books WHERE title = 'To Kill a Mockingbird'"
cur.execute(sql)
db.commit() #оновлення бази після додавання інформації


cur.close()
db.close()