import pickle

"""
Los pickles de Python son la mas de útiles ya que representan un objeto Python como una cadena de bytes. Se pueden hacer multitud de cosas con dichos bytes, como por ejemplo, almacenarlos en un archivo o base de datos, o transferirlos a través de una red.

La representación “pickle” de un objeto Python, se denomina archivo pickle. El archivo pickle, por tanto, se puede utilizar para distintos propósitos, como el almacenamiento de resultados para que sea utilizado por otro programa Python, o bien para crear copias de seguridad. Para obtener el objeto original de Python, simplemente tienes que “unpicklear” esa cadena de bytes.
"""


#Escribir en pickle

# lista = [1,2,3,4,5,6,7]
# fichero = open("lista.pckl","wb")# Write binary
# pickle.dump(lista, fichero)#
# fichero.close()

#Leer en pickle

# fichero  = open("lista.pckl","rb")
# lista2 = pickle.load(fichero)//Leerlo o cargarlo
# print(lista2)

#Ejemplo

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        # self.apellido = apellido,
        # self.edad = edad
    def __str__(self):
        return f"{self.nombre}"
        # return f"{self.nombre}{self.apellido}, edad {self.edad}"

nombres = ["Eublan", "Maria", "Guillermo"]

personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)
    
# Crear con pickle
# fichero = open("personas.pckl","wb")
# pickle.dump(personas, fichero)
# fichero.close()

#Leer con pickle
fichero = open("personas.pckl","rb")
personas = pickle.load(fichero)
fichero.close()

for p in personas:
    print(p)

