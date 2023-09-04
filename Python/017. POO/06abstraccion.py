"""
Abtraccion: La abstracción es un termino que hace referencia a la ocultación de la complejidad intrínseca de una aplicación al exterior, centrándose sólo en como puede ser usada, lo que se conoce como interfaz

Ayuda a la documentacion, ayuda a tener un mejor control sobre como vas a ir armando tu estructura

LA clase abstracta ayuda a crea una clase modelo, y obligas a loas demas subclases a seguir ese molde espesifico.

"""

from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def __init__(self,name,age,sex,talent):
        self.name = name
        self.age = age
        self.sex = sex
        self.talent = talent

    @abstractclassmethod
    def do_talent(self):
        pass
       
    def introduce(self):
        print(f"Helo Im {self.name}")
       

class Artist(Person):
    def __init__(self,name,age,sex,talent):
        super().__init__(name,age,sex,talent)

    def do_talent(self):
        print(f"I'm an Artisn and I'm {self.talent}")

class Developer(Person):
    def __init__(self,name,age,sex,talent):
        super().__init__(name,age,sex,talent)

    def do_talent(self):
        print(f"I'm developer and I'm learning {self.talent}")


charles =  Artist("charles",23,"male","Drawing")
louis = Developer("Louis",32,"female","Backend")

print("=== Charles ===\n")
#Charles
charles.introduce()
charles.do_talent()
print("=== Louis ===\n")
#Louis
louis.introduce()
louis.do_talent()


