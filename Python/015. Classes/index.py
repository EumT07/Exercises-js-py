"""
Class: es como un molde que permite crear objetos (instancias de clases, hace referencia a la memoria del ordenador solo cuando el programa esta en marcha, se crea apartir de una clase)

type() --> muestra el tipo de dato

"""

class Icecream:
    pass

cocoIcecream = Icecream()
type(cocoIcecream)# __main__.Galleta

#Creating a new class

class Car:
    new = True
    def __init__(self,model,color,tires):
        self.model = model
        self.color = color
        self.tires = tires
        print(f"model: {model} , color: {color} tires: {tires}")

    def usado(self):
        self.new = False

    def precio(self):
        if(self.new):
            print("This carr is new")
        else:
            print("This car is old")

car1 = Car("mustang","white",4)
print(car1.new)
print(car1.precio)