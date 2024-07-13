# counter() --> contar objetos, para saber cuantas veces se repite un elemento

from collections import Counter

# Ordenar dictionarios
from collections import OrderedDict

#NamedTupla()
from collections import namedtuple

"""       Test Area           """

l = [1,2,3,1,2,1,2,3,1,1]

r = Counter(l)
print(r) # 1: 5 veces, 2: 3 veces, 3: 2 veces, 1: 1 veces


word = "palabra"
r = Counter(word)
print(r) # a: 3, p: 1, l:1, b:1, r:1


#Usando creando una lista usando split (VA a separar todos en una lista)y cotando objetos repetidos

animales = "gato vaca perro gato alacran gato chivo vaca perro chivo vaca vaca"

r = Counter(animales.split())
# Vaca: 4, Gato : 3, perro: 2, chivo: 2, Alacran: 1

# Metodos del Counter

# most_common(): evniando parametros, podemos saber 1 mas comun o los 2 mas comunes

print(r.most_common(1)) # Mas comun--> Vaca : 4
print(r.most_common(2)) # Dos mas comunes --> vaca : 4, gato : 3 
print(r.most_common())# Todo los elementos


# items, key and values

l2 = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l2) # te da un indice y sus valores



# Mostrara el valor y luego la cantidad 
print(c.items())
#dict_items([(10, 4), (20, 3), (30, 2), (40, 1)])

#Mostrara las llaves
print(c.keys())
#dict_keys([10, 20, 30, 40])

#Mostrar el valor de la llaves
print(c.values())
#dict_values([4, 3, 2, 1]) 

# # Sumar todos los valores

sum(c.values()) #10

# transformar una lista:
newList = list(c)
print(newList)


newDict = dict(c)
print(newDict)

newSet = set(c)
print(newSet)


#  Creando un diccionario y respetando el orden
"""
Los dictionarios: Desordenados
"""
n = {}
n["uno"] = "One"
n["dos"] = "Two"
n["tres"] = "Three"
print(n) # {"dos":"two","tres":"three","uno":"one"}

"""
Los dictionarios: Ordenados
"""
n1 = OrderedDict()
n1 = {}
n1["Uno"] = "One"
n1["Dos"] = "Two"
n1["Tres"] = "Three"
print(n)# [("uno":"one"),("dos":"two"),("tres":"three")]


# Tuplas con nombres : namedTuplas

Persona = namedtuple("Persona", "nombre apellido edad")
p = Persona(nombre="Eublan",apellido="Mata",edad=30)
print(p)
print(p.nombre)
print(p[1])
print(p.edad)







