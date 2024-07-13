import sqlite3

# conexion = sqlite3.connect("alumnos.db")
conexion = sqlite3.connect("alumnosautoincrement.db")

cursor = conexion.cursor()


#=======================================================
#    Crear La tabla 
#=======================================================
"""
PRIMARY KEY : Permiteque no se repita el mismo valor
UNIQUE: Valor unico
"""


cursor.execute("""
    CREATE TABLE alumnos (
        dni VARCHAR(9) PRIMARY KEY,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
""")

# Creamos a los usuarios

alumnos  = [
    ('546987A','Eublan',30,'eublanmata@gmail.com'),
    ('345235B','Mario',25,'mariobros@hotmail.com'),
    ('234567B','Alicia',22,"aliciaensotel@gmail.com"),
    ('564321C','Ruben',32,'rubentegere@gmail.com')
]

# Insertamos los usuarios dentro de la tabla

cursor.executemany("INSERT INTO alumnos VALUES (?,?,?,?)", alumnos)

# Insertarmos un usuario aparte con otro dni y vemos la nuevaposicion


cursor.execute("INSERT INTO alumnos VALUES ('333333B','Alicia',22,'aliciaensotel@gmail.com')")


#==========================================================
# Nueva tabla para productos, incrementar su id
#==========================================================


cursor.execute("""
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        marca VARCHAR(50) NOT NULL,
        precio FLOAT NOT NULL
    )
""")

# Creamos a los usuarios

productos = [
    ('Teclado',"logitech",70.45),
    ('Monitor 19','LG',60),
    ('Mouse Gamer',"logitech",15.66)
]

# Insertamos los usuarios dentro de la tabla
# Se coloca null para que automatica mente comience en 1 y se vaya incrementando

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)


#Consultar un producto

cursor.execute("SELECT * FROM productos")

productos = cursor.fetchall()
for x in productos:
    print(x)


"""
Auto increment examples

"""

cursor.execute("""
    CREATE TABLE alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
""")

alumnos  = [
    ('546987A','Eublan',30,'eublanmata@gmail.com'),
    ('345235B','Mario',25,'mariobros@hotmail.com'),
    ('234567B','Alicia',22,"aliciaensotel@gmail.com"),
    ('564321C','Ruben',32,'rubentegere@gmail.com')
]

cursor.executemany("INSERT INTO alumnos VALUES (NULL,?,?,?,?)", alumnos)

# Añadir un nuevo usuario

cursor.execute("INSERT INTO alumnos VALUES (null, '234567B','Alicia',22,'aliciaensotel@gmail.com')")

conexion.commit()
conexion.close()