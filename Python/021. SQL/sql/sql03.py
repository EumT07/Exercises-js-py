import sqlite3

conexion = sqlite3.connect("productos_autoincrement.db")
cursor = conexion.cursor()

# cursor.execute("""
#     CREATE TABLE productos(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
# """)

# product_list = [
#     ('0102-M19A','Monitor','Samsung',45.23),
#     ('0103-T44A','CPu i5','Asus',99.99),
#     ('0114-G-9A','Compresor','Monlanch',35),
#     ('1111-ER-A','Escritorio','wood',60.53),
#     ('0456-J69A','Jumper','Jump',39.99)
# ]

# cursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?,?)", product_list)


"""
WHERE

#Buscar campos unicos

"""

# id

cursor.execute("SELECT * FROM  productos WHERE id=2")

# dni

cursor.execute("SELECT * FROM  productos WHERE dni='0456-J69A'")


"""
Where: para ubicar por tag 
"""

cursor.execute("SELECT * FROM productos WHERE precio= 60.0")


products = cursor.fetchall()

# for product in products:
print(f"Productos: {products}")

"""
Update

UPDATE productos SET
"""

cursor.execute("UPDATE productos SET nombre='Black Desk', precio = 50 WHERE dni='1111-ER-A'")

cursor.execute("SELECT * FROM productos WHERE dni='1111-ER-A'")

productEdit = cursor.fetchone()
print(productEdit)


"""
Delete

Nunca olvidar colocar el WHERE* , PARA EVITAR BORRAR todo

DELETE FROM "databasename" WHERE

"""

cursor.execute("DELETE FROM productos WHERE dni='0114-G-9A'")

cursor.execute("SELECT * FROM productos")

products = cursor.fetchall()

for product in products:
    print(product)


conexion.commit()
conexion.close()


"""
SQL investigar:

Consultas mas avanzadas: or, and, like, join
Funciones simples: count, group by, distinct
Funciones Avanzadas: Sum, AVG, min, max
Manejo de fechas: Date, year, month, day
Relaciones y Claves Fóraneas

"""


