import sqlite3

def crear_db():
    conexion = sqlite3.connect("restaurant.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)""")
    except sqlite3.OperationalError:
        print("La tabla 'categoria' ya existe.")
    else:
        print("La tabla 'categoria' se ha creado correctamente.")

    try:
        cursor.execute("""
            CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))""")
    except sqlite3.OperationalError:
        print("La tabla 'plato' ya existe.")
    else:
        print("La tabla 'plato' se ha creado correctamente.")

    conexion.close()

#Add categoria
def agregar_categoria():
    categoria = input("¿Nombre de la categoria? \n\n>")

    conexion = sqlite3.connect("restaurant.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(f"INSERT INTO categoria VALUES (null, '{categoria}')")
    except sqlite3.IntegrityError:
        print(f"La categoria '{categoria}' ya existe..")
    else:
        print(f"La categoria '{categoria}' ha sido creado correctamente")

    conexion.commit()
    conexion.close()

#Add Platos

def agregar_plato():
    
    conexion = sqlite3.connect("restaurant.db")
    cursor = conexion.cursor()

    #REvisamos la base de dato para mostrar las categorias
    categorias =  cursor.execute("SELECT * FROM  categoria").fetchall()
    print("Selecciona una categoria para añadir el plato")
    for categoria in categorias:
        print(f"[{categoria[0]}] {categoria[1]}")
    #categoria[0] --> es el id
    #categoria[1] --> el nombre de la categoria
    categoria_usuario = int(input("\n> "))

    plato = input("¿Nombre del plato?\n>")

    try:
        cursor.execute(f"INSERT INTO plato VALUES (null, '{plato}', {categoria_usuario})")
    except sqlite3.IntegrityError:
        print(f"El plato '{plato}' ya existe..")
    else:
        print(f"El Plato '{plato}' ha sido creado correctamente")

    conexion.commit()
    conexion.close()

def mostrar_menu():
    conexion = sqlite3.connect("restaurant.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id={categoria[0]}").fetchall()
        for plato in platos:
            print(f"\t{plato[1]}")
    print("\n")

#Crear la base de datos
crear_db()

#Menú de opciones
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input("\nIntroduce una opcion:\n[1] Agregar un categoria\n[2] Agregar un Plato\n[3] Mostrar Menú\n[4] Salir de la app\n\n> ")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
        break
    elif opcion == "4":
        print("Gracias, Vuelve pronto..!!")
        break
    else:
        print("Opción incorrecta")











