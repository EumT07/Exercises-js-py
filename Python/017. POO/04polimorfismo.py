"""
La palabra polimorfismo proviene del griego y significa que posee varias formas diferentes. Es uno de los conceptos esenciales de la programación orientada a objetos. Así como la herencia está relacionada con las clases y su jerarquía, el polimorfismo lo está con los métodos.
"""

class Cat:
    def sound(self):
        return "Miau"

class Dog:
    def sound(self):
        return "Guau"

cat = Cat()
dog = Dog()

#The same methods but diferent objects

print(cat.sound())
print(dog.sound())

#Duck typing: 
# Enlaces dinamisoc y estaticos
# tipo real
# tipo declarado 