
"""
1 Part Conceptos Basicos

Fichero: Conjunto de bits almacenados en un dispositivoi de memoria persistente (Disco duro), indentificado, con un nombre, una dirreccion a la ruta que lo contiene y un extension. Archivos informaticos, se identifican con una extension.

Operacion: Creacion Apertura Cierre Extension (.txt .word .py)

Puntero: Representa el lugar donde apunta el fichero antes de realizar una operacion determinada, seria como el lugar donde ponemos nuestro dedo o fijamos la vistea mientras leemos o escribimos

Ficheros de textos: guardan datos en forma de texto plano, son entendible por las personas.

Ficheros binarios: Lenguaje codigo/maquina --> 0 - 1 - 0 - 1 - 1

r --> Solo lectura
w --> Escritura, si ya existe el fichero, machaca o elimina su contenido por uno nuevo.
a --> adicion: Solo esribe, si ya existe el fichero, todo lo que se escriba se añadira al final
x --> Es como w, pero si existe el fichero lanza una excepcion
r+ --> Lecuta y escritura.


es importante abrir y cerrar el fichero

from io import open : scripts

"""

"""
1 Part Ficheros de texto
"""

""" Creat - Crear o escribir fichero """

# texto = "Esta linea es desde fichero creado\nOtra linea creada para poder escribir de nuevo"

# fichero = open("fichero.txt","w")
# fichero.write(texto)
# print(fichero)
# fichero.close()

"""Si ya existe va eliminar lo anterior y lo va actualizar"""
#--------------------------------------------#


""" Read - Leer un fichero """
 
# fichero = open("fichero.txt","r")
# texto = fichero.read()
# fichero.close()
# print(texto)

#--------------------------------------------#


""" Read Lines --> Leer varias lineas """

# fichero = open("fichero.txt","r")
# lineas = fichero.readlines()
# fichero.close()
# print(lineas)
# print(lineas[0])
# print(lineas[-1]) #Obtener la ultima

#--------------------------------------------#

""" Read lines --> extension o modo Append"""
#El puntero se va posicionar al final de todo

# fichero = open("fichero.txt", "a")
# fichero.write("\nCuarta lineas")
# fichero.close()
# Va introducir una cuarta lineas

"""Si se intenta abrir un fichero en modo lectura "r", dara un error, pero con "a", si lo va crear """
#--------------------------------------------#

""" read Line --> Leer una linea x linea """

# fichero = open("fichero.txt","r")
# l = fichero.readline()
# print(l)#Esta linea es desde fichero creado

# l = fichero.readline()
# print(l)#Otra linea creada para poder escribir de nuevo

# l = fichero.readline()
# print(l)#Tercera linea

# l = fichero.readline()
# print(l)#Esta es la cuarta linea agregada

# fichero.close()

#--------------------------------------------#

"""El puntero siempre va avanzar al final de la ultima linea en este caso, si hay mas de 2"""

""" Recorrer las lineas con for """

# with open("fichero.txt","r") as fichero:
#     for linea in fichero:
#         print(linea)


#-------------------------------------------------#


"""
2 Part Manejo del puntero

"""

""" Write - Agregar un nuevo Contenido """

# newContent = "\n Esta es la cuarta linea agregada"
# fichero = open("fichero.txt","a")
# fichero.write(newContent)
# fichero.close()

#--------------------------------------------#

"""
Manejo del puntero, permite buscar dentro de los caracteres ciertas posiciones para poder editar, leer, el puntero en este caso seria la linea que titila. 

"""
#Part 1

# seek(): Permite posicionar el puntero, de acuerdo al caracter donde se encuentre.

# fichero = open("fichero.txt","r")
# fichero.seek(10) # Caracter numero 10
# fr = fichero.read()
# print(fr) 

"""
es desde fichero creado
Otra linea creada para poder escribir de nuevo
Tercera linea
Esta es la cuarta linea agregada
"""

#Part 2
#read(): Permite leer y posiciona el puntero al final de caracter, ya leido.

# fichero.read(5)#
# fr = fichero.read()
# print(fr)

"""
linea es desde fichero creado
Otra linea creada para poder escribir de nuevo
Tercera linea
Esta es la cuarta linea agregada
"""
#--------------------------
#fichero.seek(len(texto)/2) --> 45.0 te ubicara en el caracter con ese numero. 

#fichero.seek( len(fichero.readline())) #--> Permite posicionarte al final de todo el texto dentro del fichero

#--------------------------

"""
Reescrbiniendo
"""

# r+ (Lectura y escritura): se posicionara al principio del fichero, y va reemplezar todo ese contenido

# fichero = open("fichero.txt","r+")
# fichero.write("dfasdfa")
# fichero.close()

# r+ y usando funcion readlines() para acceder a las lineas como si fueras listas

# fichero = open("fichero.txt","r+")
# lineas = fichero.readlines()
# lineas[2] = "Esto fue editado para reeemplezar \"Tercera Linea\" \n"
# fichero.seek(0)
# fichero.writelines(lineas)
# fichero.close()

# a es la cuarta linea agregada, --> debido que anteriormente cuando sobreescribio, como u elimino las primeras letras


