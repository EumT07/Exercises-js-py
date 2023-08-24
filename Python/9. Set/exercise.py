"""
Realiza un programa que siga las siguientes instrucciones:

    Crean un conjunto llamado usuario con los usuarios ; Marta, David, Elvira, Juan y Marcos
    crea un conjunto llamado administradores con los adminisradores Juan y marta
    Borra al administrador Juan del conjunto de administradores
    Añade a marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios
    Muestra todos los usuarios por pantalla de forma dinamica, ademas debes indicar cada usuarios es administrador o no.

Nota: Los conjuntos se puden recorrer dianamicamente utilizando el bucle for de forma similar a una lista. Tambien cuentan con un metodo llamado .discard(Elemetno) que sirve para borrar un elemento.
"""
from collections import deque

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}

# Eliminamos a juan del conjunto de administradores e introducimos a Marcos.

administradores.discard("Juan")
administradores.add("Marcos")

#  Mi punto de vista con deque

cola = deque(administradores)

cola.popleft()# Juan out
cola.append("Marcos")

# Recorrer usuarios hizo el ejercicio mas simple

# for usuario in usuarios:
#     if usuario in administradores:
#         print(f"{usuario} es Admin")
#     else:
#         print(f"{usuario} no es admin")

"""
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

    El caballero tiene el doble de vida y defensa que un guerrero
    El guerro tienes el doble de ataque y alcance que un caballero
    El arquero tienes la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance
    Muestran como queda las propiedades de los tres personajes

"""

caballero = {"vida":2, "ataque":2,"defensa":2,"alcance":2}
guerrero = {"vida":2, "ataque":2,"defensa":2,"alcance":2}
arquero = {"vida":2, "ataque":2,"defensa":2,"alcance":2}

# (correcta)

#Caballero
caballero["vida"] = guerrero["vida"] * 2 # 4
caballero["defensa"] = guerrero["defensa"] * 2 # 4
#Guerrero
guerrero["ataque"] = caballero["ataque"] * 2 # 4
guerrero["alcance"] = caballero["alcance"] * 2 # 4
#Arquero
arquero["vida"] = guerrero["vida"] # 4
arquero["ataque"] = guerrero["ataque"] # 4
arquero["defensa"] = guerrero["defensa"] / 2 # 2  
arquero["alcance"] = guerrero["alcance"] * 2 # 8


# List

# teams = [
#     {"Caballero":caballero},
#     {"Guerrero":guerrero},
#     {"Arquero":arquero}]

# Diccionario
teams = {
    "Caballero":caballero,
    "Guerrero":guerrero,
    "Arquero":arquero}

# For para recorrer
# for team in teams:
#     print(team,teams[team])


"""
Durante la planificacion de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad(cuanto menor es el numero de orden, mas prioridad)

¿Eres capaz de crear del tipo cola con todas las areas pero sin numeros de orden?

Para ordenar automaticamente una pista posible utiliza sort

"""

tareas = [
    [6, "Distribucion"],
    [2, "Diseño"],
    [1, "Concepcion"],
    [7, "Mantenimiento"],
    [4, "Produccion"],
    [3, "Planificacion"],
    [5, "Pruebas"],
]

# print("Desordenadas")

for tarea in tareas:
    print(tarea[0], tarea[1])

from collections import deque

print("Tareas Ordenadas")

tareas.sort()

print("Tareas ordenadas sin deque")
for tarea in tareas:
    print(tarea[1])

#Order con deque

cola = deque()
print("Tareas ordenadas con deque")
for tarea in tareas:
    cola.append(tarea[1])

print(cola)

for tarea in cola:
    print(tarea)