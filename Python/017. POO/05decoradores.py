"""
Decoradores permite agregar nuevas funcionalidades a un funciones antes o despues de ejecutarlas
"""

# def decorador(funcion):
#     def funcion_modificada():
#         print("Antes de llamar a la funcion")
#         funcion()
#     return funcion_modificada

# @decorador
# def saludo():
#     print("Hellooo")

# saludo()

#Decorador property

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @name.deleter
    def name(self):
        del self.__name

jhon = Person("jhon",27)

name = jhon.name
print(name) 

name = jhon.name = "Guille"
print(name) 