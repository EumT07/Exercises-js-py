from io import open
import sys
"""
Crear un script llamado contador y que realice varias tareas sobre un fichero llamado contador.txt que almacenara un contador de visistas.


Nuevo escript trabajar sobre un fichero contador.txt. Comprobaremos si el fichero no existe o esta vacio, en se caso lo crearemos con el numero 0. si existe simplemente leeremos el valor del contador
Luego apartir de un argumento:
    si se envia el argumento inc, se incrementara el contador en uno y se monstsrar por pantalla
    si se envia el argumento dec, se decrementara el contador en uno y se monstrara por pantalla.
    si no se envia ningun argumento (o el valor que no sea inc o dec), semostrara el valor del contador por pantalla
Finalmente guardara de nuevo el valor del contador de  nuevo en el fichero.
Utiliza excepiones si cree que es necesario, puedes mejorar el mensaje: error: Fichero corrupto

"""

# Creamos 
fichero = open("contador.txt", "a+")
fichero.seek(0)
contenido = fichero.readline()


if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)
    
#Intentamos transformar el texto a un numero
try:
    contador = int(contenido)# "0" --> 0
    #Funcion de inc o dec
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
    print(contador)

    #Escribimos los cambios en el fichero
    fichero = open("contador.txt","w")
    fichero.write(str(contador))# Numero -> string


except:
    print("Erro del fichero..")





