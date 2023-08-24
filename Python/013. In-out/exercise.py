"""
Formatee los siguientes valores para mostrar el resultado idicado
    "Hola mundo" -> Alineador a la derecha 20 caracteres
    "Hola mundo" -> Truncamiento en el cuarto caracter index 3
    "Hola mundo" .> Alineamiento al centro en 20 caracteres con truncamiento en el segundo caracteres indice 2
    150 formato de 5 numeros enteros rellenados con 0
    7887 fomateo a 7 numeros entrenos rellenados con espacios
    20.02 formateo a 3 numeros y 3 decimales.

"""

#
h = "Hola mundo"

print(f"{h:>20}")
print(f"{h:.3}")
print(f"{h:^20.1}")
print("{:05d}".format(150))
print("{:7d}".format(7887))
print("{:07.3f}".format(20.02))

"""
Crea un script llamado tabla.py que realice las siguientes tareas
    1- Debe tomar 2 argumentos, ambos numeros enteros positivos   de 1 al 9, si no mostrara un error
    2- El primer argumento hara referenci a las listas de una tabla, el segundo en columnas de tablas
    3- En caso de no recibir uno o ambos argumentos, debe mostrar informacion de como usar el escript
    4- el script contendra un bucle for que intere el numeros de veces del primer argumento
    5- dentro del for, añade un segundo for que itere el numero de veces del segundo argumento
    6- dentro del segundo for ejecuta una instruccion print("", end="), (env=envita un salto de linea)
    7-ejecuta el codigo y observa el resultado.

    Ahora intenta deducir donde, y como añadir otra instruccion print para dibujar un tabla
     recordatorio; los argumentos se envian como cadenas separadas por espacios Si quieres enviar un mensaje, deberas introducirlos en comillas dobles "Esto es un argumento"- Para capturas los argumentos debes utilizar lo siguientes: import sys , print(sys.argv)

     Esto estara en la tabla.py

"""


#3

"""
Crea un script llamado descomposicion.py que realice las siguientes tareas

    1- Debe tomar un argumento que sera un numero enero postivo
    2-En caso de no recibir un argumentos, debe mostrar informacion acerca de como utilizar el script

El objetivo del escrip es decomponer en numero en unidades, decenas, centenas, miles, tal como por ejemplo se introduce el numero > 3647

El programa debera devolver una descomposicion linea a linea como la siguiente utilizando las tecnicas de formateo

0007
0040
0600
3000

Pista: Que el valor sea unnumero no significa necesariamente que deba serlo para formatealos. Necesitas jugar muy bien con los indices, y hacer muchas conversioes entre tipo de cadenas numeros y viceversa.

"""