import sqlite3

#Crear nuestra base de dato
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

#Crear la primera tabla: usuarios sera nuetra base de dato inicial

"""
Crear: una tabla para poder realizar el proceso de registro de usuarios = nombre de la tabla

CREATE TABLE usuarios (nombre VARCHAR(100),edad INTEGER, email VARCHAR(100))

"""
########################### CREAT #############################

cursor.execute("""
    CREATE TABLE usuarios (
    nombre VARCHAR(100),
    edad INTEGER, 
    email VARCHAR(100)
    )""")

###############################################################



"""
Insertar un usuario dentro de la tabla

INSERT INTO usuarios VALUES ('Eublan', 30,'eublanmata@gmail.com')

"""

############################ Insert ############################

cursor.execute("""INSERT INTO usuarios VALUES (
    'Eublan, 
    30,
    'eublanmata@gmail.com')""")

###############################################################

"""
Poder Seleccionar el usuario dentro de la tabla

SELECT * FROM usuarios
* trae todos los usuarios

"""
######################## Seleccionar ###########################

cursor.execute("SELECT * FROM usuarios")
print(cursor) #Debemos transformar en un objeto para poder leer

###############################################################

"""
Asignar el valor dentro la tabla a una variable para poder obtener el usuario

"""
###############################################################

usuario = cursor.fetchone()#Traera al usuario --> 1er registro

###############################################################


"""
Insertar mas de 1 usuario a una tabla

Primero creamos los usuarios y luego introducimos con el executeall()

"""
###############################################################

#HAcer una lista de varios usuarios para un ingreso masivo

# usuarios = [
#     ('Miguel',28,'miguelito28@gmail.com'),
#     ('Andrea',32,'andreinamartinez@gmail.com'),
#     ('Salu',45,'saulramirez@gmail.com')
# ]

# #Insertar varios usuarios

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

###############################################################

"""
Recuperamos los datos almacenados 
"""
###############################################################

#Recuperar o mostrar los datos almacenados

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()#Traera todos los usuarios 

for user in usuarios:
    print(f"Nombre: {user[0]} - Edad:{user[1]} - Email: {user[2]}") 

###############################################################

#Ejecuta la accion de comentar, para confirmar los cambios realizados
conexion.commit()
# At the end
conexion.close()
