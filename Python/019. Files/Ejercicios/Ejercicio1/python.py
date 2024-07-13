from io import open
"""
Ejercicio 1: 

Deberas crear un script llamado persona.py que LEA (Osea va leer no a crear) los datos de un fichero de texto(Ya creado), que transforme cada fila en un diccionario y lo añada a una lista llamada persona. Luego recorre las personas de la lista y para cada una muestra de forma amigable todos sus campos. 

El fichero de texto se denominara, personas.txt y tendra el siguiente contenido en texto plano(crealo previamente)

1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4:David;García;25/07/2006

los campos tendran el siguiente orden: id nombre aprellido y nacimiento

Aviso: Si quieres leer un fichero que no se ha escrito directamente con python, entonces es posible que encuentres errores de codificacion al  mostrar algunos caracteres. Asegurate de indicar la codificacion del fichero manualmente durante la apertura como argumento en el orden, por ejemplo con UTF-8

open(...; encodigin="utf-8")

"""

#Fichero

fichero = open("personas.txt","r", encoding="utf-8")
lineas = fichero.readlines()
fichero.close()

#Creamos la lista de personas
personas = []

#Recorremos cada linea, para transformarlos en diccionario
for linea in lineas:
    linea = linea.replace("\n","")#Buscara: \n y lo reemplazara ""
    campos = linea.split(";")#--> TRansforma en una lista.
    #Creamos el diccionario
    persona = {"id":campos[0],"nombre":campos[1],"apellido":campos[2],"nacimiento":campos[3]}
    personas.append(persona)

# Recorremos Persona -> 1

# for p in personas:
#     print(p)

#Recorrer Persona -> 2

for p in personas:
    print( f"(id = {p['id']}) -> {p['nombre']} {p['apellido']} ==> {p['nacimiento']}"  )

