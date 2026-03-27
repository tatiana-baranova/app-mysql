import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="my_data"
)

cur = db.cursor()

# sql = "CREATE TABLE users(
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   login VARCHAR(50),
#   pass VARCHAR(55) NOT NULL
# )"
# cur.execute(sql)

# sql = "INSERT INTO users(login, pass)VALUES(%s, %s)"
# user= [
#     ('John', 'some_pass'),
#     ('Alex', 'some_pass')
# ]
# cur.executemany(sql,user)
# db.commit()


# sql = "SELECT * FROM users WHERE login = 'John'"
# cur.execute(sql)
#
# res = cur.fetchall()
# for el in res:
#     print(el)



# sql = "CREATE TABLE items(
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   title VARCHAR(50) NOT NULL,
#   price INT(3),
#   category VARCHAR(10)
#   )"
# cur.execute(sql)

# sql = "INSERT INTO items(title, price, category)VALUES(%s, %s, %s)"
# item= [
#     ('Кружка чоловіча', '300', 'cups'),
#     ('Кепка червона', '150', 'hats'),
#     ('Кепка синя', '200', 'hats'),
#     ('Кружка жіноча', '400', 'cups'),
#     ('Червона футболка', '550', 'shirts'),
#     ('Футболка "Рік і Морті"', '700', 'shirts')
# ]
# cur.executemany(sql,item)
# db.commit()

# sql = "SELECT * FROM items WHERE category = 'hats'"
# cur.execute(sql)
#
# res = cur.fetchall()
# for el in res:
#     print(el)


# sql = """
# CREATE TABLE orders (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT,
#     item_id INT,
#     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
#     FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE
# )
# """
# cur.execute(sql)


# sql = """
# INSERT INTO orders (user_id, item_id)
# SELECT users.id, items.id
# FROM users
# JOIN items
# WHERE users.login = 'John' AND items.category = 'hats';
# """
# cur.execute(sql)
# db.commit()

res= """
SELECT users.login, items.title
FROM orders
JOIN users ON orders.user_id = users.id
JOIN items ON orders.item_id = items.id
"""
cur.execute(res)
orders = cur.fetchall()
print('Всі замовлення')
for order in orders:
    print(f"{order[0]} - {order[1]}")

cur.close()
db.close()