"""
Realiza una funcion llamada area_rectangulo(), que devuelva el area del rectacgulo apartir de una base y una altura.
    base 15
    altura 10

"""
#datos
base = 15
altura = 10

def area_rectangulo(base,altura):
    return base * altura

result1 = area_rectangulo(base, altura )
print(result1)

"""
Realiza una funcion llamada, area_circulo() que devuelva el area de un cirulo apartir de un radio, area del circulo de 5 anchos
    El area de un circulo se obtiene elevando al cuadrado el radios y multiplicando el resultado por pi, puedes usar el pi como 3.14159 o importando math
"""

# ancho de altura
ancho = 5
import math 

def area_circulo(a):
    radio = a**2
    return radio * math.pi #3.14159

result2 = area_circulo(ancho)
print(result2)

"""
Realiza una funcion llamada relacion(), que apartir de dos numeros realice las siguientes funciones:
    si el primer numero es mayor que el segundo, debe volver 1
    Si el primer numero es menor que el segundo, debe devolver -1
    Si ambos numeros son iguales, debe devolver un 0

"""

def relacion(num1, num2):
    if num1 > num2:
        print("1")
    elif num1 < num2:
        print("-1")
    else:
        print("0")
result3 = relacion(10,20)#-1
result3 = relacion(5,5)# 0

"""
Realice una funcion llamada intermedio(), que a partir de dos numeros, devuelve su punto intermedio
    Nota: numero intermedio es la suma de dos numeros entre dos
"""

def intermedio(num1,num2):
    return (num1 + num2) / 2
result4 = intermedio(-12,24)
print(result4)

"""
Realiza una funcion llamada recortar(), que reciba tres parametros, el primero es un numero a recortar, 2 limite inferir, 3 limite superior:
    devolver el limite inferior si el numero es menor a este
    devolver el limite superior si el numero es mayor que este
    devolver el numero sin cambios si no se supera ningun limite
"""

def recortar(num, limiteInf, LimiteSup):
    if num < limiteInf :
        return limiteInf
    elif num > LimiteSup:
        return LimiteSup
    else:
        return num

# rsl = recortar(15,0,10)
rsl = recortar(8,0,10)
print(rsl)

"""
Realiza una funcion separar() que tome una lista de numeros enteros, y que devuelva dos lista, 1 con numeros enteros y otra con numeros pares

"""
lista_num = [-12, 84,13,20,-33,101,9]
lista_n2 = [0,1,2,3,4,5,6,7,8,9,10,11]

def separar(lista):
    lista.sort()
    par = []
    impar = []
    for n in lista:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    return par, impar

par, impar = separar(lista_n2)# Destructurando o asignando ambos resultados a las variables par e impar
print(par)
print(impar)