"""
Vehivulo ( color, ruedas)

coche (velocidad y cilindrada)

"""

# class Vehiculo():
#     def __init__(self, color, ruedas):
#         self.color = color
#         self.ruedas = ruedas
#     def __str__(self):
#         return f"color {self.color}, {self.ruedas} de ruedas"


# class Coche(Vehiculo):
#     def __init__(self,color,ruedas,velocidad,cilindrada):
#         self.color = color
#         self.ruedas = ruedas
#         self.velocidad = velocidad
#         self.cilindrada = cilindrada
#     def __str__(self):
#         return f"El coche es de; color: {self.color}, {self.ruedas} ruedas,{self.velocidad} km/h y una cilindrada de {self.cilindrada} cc"


# c = Coche("White",4,200,1800)
# print(c)

"""
Truco super class: es llamar directamente a la classe."metodos"(self)
"""
# class Vehiculo():
#     def __init__(self, color, ruedas):
#         self.color = color
#         self.ruedas = ruedas
#     def __str__(self):
#         return f"El coche es de: color {self.color}, {self.ruedas} de ruedas"


# class Coche(Vehiculo):
#     def __init__(self,color,ruedas,velocidad,cilindrada):
#         #Nos traemos el constructor de vehiculo
#         Vehiculo.__init__(self,color,ruedas)
#         self.velocidad = velocidad
#         self.cilindrada = cilindrada
#     def __str__(self):
#         return Vehiculo.__str__(self) + f"{self.velocidad} km/h y una cilindrada de {self.cilindrada} cc"


# c = Coche("White",4,200,1800)
# print(c)

""" Recomendado """

"""
Super, nos ayuda hacer lo anterior sin utilizar self
"""

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f"Color {self.color}, {self.ruedas} de ruedas"


class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)# super() sin self
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + f"{self.velocidad} km/h y una cilindrada de {self.cilindrada} cc"


c = Coche("White",4,200,1800)
print(c)


"""
Ejercicio: extender la clase vehiculo y realiza la siguiente implementacion: 

                        Vehiculo (color y ruedas)

coche(velocidad y cilindrada)                     Bicicleta --> tipo(urbana/deportiva)
camioneta(carga)                                  Motocicleta(velocidad,cilindrada)


Expeirimente

Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos
Realiza un funcion llamada catalogar() que reciba una lista y los recorra mostrando el nombre de su clase y sus atributos
Modifica la funcion catalogar() para que reviba un argmuento optativo ruedas, haciendo, que muestre unicamente los que su numero de rueda concuerde con el valor del argumento. Tambien dede mostrar un mensaje "Se han encontrado {} vehiculos con {} ruedas:" Unicamente si se envia el argumento ruedas. Ponla a prueba cin 0, 2, y 4 ruedas como valor 

Atributo especial de la clase name
"""

class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada, carga):
        super().__init__(color,ruedas,velocidad,cilindrada)# super() sin self
        self.carga = carga
    def __str__(self):
        return "La camioneta es de color: " + super().__str__() + f" y soporta {self.carga} kg"

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)# super() sin self
        self.tipo = tipo
    def __str__(self):
        return "La Bicicleta es de color: " + super().__str__() + f" {self.tipo}"

class Motocileta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo)# super() sin self
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "La motocicleta es de color: " + super().__str__() + f" {self.velocidad} km/h y una cilindrada de {self.cilindrada} cc"

vehiculos = [
    Coche("Blanco",4,200,1200),
    Camioneta("Azul",4,150,1800,1200),
    Bicicleta("Negra",2,"Urbana"),
    Motocileta("Roja",2,"Deportiva",220,1800)
]

# def catalogar(lista):
#     for v in lista:
#         print(f"{type(v).__name__}, {v}")

def catalogar(lista, ruedas=None):
    if ruedas != None:
        contador = 0
        for v in lista:
            if v.ruedas == ruedas:
                contador += 1
        print(f"Se han encontrado {contador} vehiculos con {ruedas} ruedas:")

    for v in lista:
        if ruedas == None:
            print(f"{type(v).__name__}, {v}")
        elif v.ruedas == ruedas:
            print(f"{type(v).__name__}, {v}")

catalogar(vehiculos,2)