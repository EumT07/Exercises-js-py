"""
Plano cartesiano: Plao bidimensional, 2 dimenciones

Ejercicio:
Crea una clase llamada punto con sus dos coordeanadas X e Y
Añade un metodo contructor para crear puntos facilmente. Si no se reciben una coordenada, su valor sera cero
Sobrescribe el metodo string, para imprimir por pantalla un punto que apaerezca en formato (X,Y)
Añade un metodo llamado cuadrante que indique a que cuadrante pertenece el punto, o si es el origen
Añade un metodo llamado vector que tome otro punto, y calcule el vector resultante entre los dos puntos
(optativo)Añade un metodo llamado distancia, que tome otro punto y cakcuke ka distancia entre los dos puntos y la muestre por pantalla.

"""


"""
Crea una clase llamada rectangulo con dos puntos (inicial y final) que forman la diagonal del rectangulo.
Añade un metodo constructor para crear ambos puntos facilmente, si no se envian, se crearan dos puntos en el origen por defecto
añade el rectangulo un metodo llamado base que muestre la base
añade el rectangulo un metodo llamado altura que muestre la alture
añade al rectangulo un metodo area que muestre la alture


"""

import math

class Punto:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    #self en el control de flujo va mostrar el siguiente codigo cuando se ejecuten las condiciones
    def __str__(self):
        return f"({self.x},{self.y})"
    def cuadrante(self):
        if(self.x > 0 and self.y > 0):
            print(f"{self}: Primer Cuadrante")
        elif(self.x < 0 and self.y > 0):
            print(f"{self}: Segundo Cuadrante")
        elif(self.x < 0 and self.y < 0):
            print(f"{self}: Tercer Cuadrante")
        elif(self.x > 0 and self.y < 0):
            print(f"{self}: Cuarto Cuadrante")
        else:
            print(f"{self}: Se encuentra en el origen")
    def vector(self, p):
        print(f"El vector entre {self} y {p} es ({p.x - self.x},{p.y - self.y})")
    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y -self.y)**2)
        print(f"La distancia entre los puntos {self} y {p} es de : {d}")


# Comprobar lo siguiente:
#A(2,3),B(5,5),C(-3,-1) y D(0,0)
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

# Ver los cuadrantes
A.cuadrante()#Primer
B.cuadrante()#Primer
C.cuadrante()#Tercero
D.cuadrante()#Origen

#Vecor A y B
A.vector(B)# --> 3,2

#Vector B y A
B.vector(A)# --> -3,-2

#Distancia, cual de los 3 puntos se encuentra mas lejos
A.distancia(D)#3.60
B.distancia(D)#7.07 --> Mas lejono.
C.distancia(D)#3.16

#Rectangulo

class Rectangulo:
    def __init__(self, pInicial = Punto(),pFinal = Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print(f"La base del rectangulo es {self.base}")
    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print(f"La base del rectangulo es {self.altura}")
    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        print(f"El area del rectangulo es {self.area}")

r = Rectangulo(A,B)
r.base() #3
r.altura() #2
r.area() #6