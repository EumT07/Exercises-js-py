"""
Encapsulacion de atributos y metodos, funcionabilidad, para impedir el acceso a los metodos. 
"""

class Ejemplo:
    __atributo_privado = print("Este es un atributo privado")
    def __metodo_privado(self):
        print("Este es un metodo privado")
    def atributo_publico(self):
        return self.__atributo_privado
    def metodo_publico(self):
        return self.__metodo_privado()
        
e = Ejemplo()
# e.__atributo_privado
# e.__metodo_privado()
e.atributo_publico()
e.metodo_publico()


#Get
#set

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

jhon = Person("jhon",27)

name = jhon.get_name()

jhon.set_name("Josh")

name = jhon.get_name()
print(name) 