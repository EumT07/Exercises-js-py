"""
Los modulos, archivos que contienen cierta informacion y permite organizarlos y usarlos nuevamente

Se debe importar del  file donde queremos obtener los datos:

-. import "name of file" 

Para importar una funcion de un modulo

-. From "name of file import "name of funcion"

Importaras todo los archivos
-. from "nameoffile" import * : 


"""

# Entramos a la carpeta -->  modulos/paquete/paquete.py
# Se logro sin usar __init__.py
#from : Carpetas y direcciones
#import: importa funciones o classes o fragmentos de codigo
from modulos.paquete.paquete import *
from modulos.test.moduloC import test

#Prestar atencion si dentro del file se llama a otros files
from modulos.moduloA import sumar

print("/modulos/paquetes/paquete.py:")
Hola("Eublan","Mata")
#"Hola Eublan Mata, sea usted bienvenido"

print("/modulos/test/moduloC.py :")
test()#"Esto proviene de la carpeta de :/test/moduloC :3

print("/modulos/moduloA.py")
sumar(3,7)
#"Hola esta funcion de sumar es del modulo A y la suma es: 10"


"""
Modulos standars :

Copy : para crear copias
Collections: deque 
datetime: Fechas y horas
doctest y unisttest: crear pruebas de testing *Leer*
html,xml,json: permite manejar estructuras de datos
pickle: trabaja con ficheros y textos
math: Funciones matematicas
re: expresiones avanzadas
random: generar contenido aleatorio
socket: enfocado en comunicacion avanzadas *Buscar*
sqlite3: sistema de base de dato
sys: conseguir informacion del entorno del sistema operatito, Avanzado
threading: dividir procesos en subprocesos: Avanzado
tkinter: interfaz graficas: formularios, botones, campos de textos

"""