"""
Realiza un programa que lea dos numeros por teclado y permita elegir entre 3 opciones con un menu, debe mostrar:

Suma de dos numeros
resta de dos numeros
mostrar una multiplicacion en caso de no introducir opcion valida el programa debe informarlo.

"""

print("Welcome to our menu: Take one option")
while(True):
    print(
    """
    Take an options: 
    1) add
    2) subsr
    3) Multly
    4) Salir
    """)
    option = input("Which option will you take?: ")
    if option == "1":
        n1 = float(input("Insert number1: "))
        n2 = float(input("Insert number2: "))
        result = n1 + n2
        print(f"Your result is: {result}")
    elif option == "2":
        n1 = float(input("Insert number1: "))
        n2 = float(input("Insert number2: "))
        result = n1 - n2
        print(f"Your result is: {result}")
    elif option == "3":
        n1 = float(input("Insert number1: "))
        n2 = float(input("Insert number2: "))
        result = n1 * n2
        print(f"Your result is: {result}")
    elif option == "4":
        print("Thanks, good bye")
        break
    else:
        print("There is an err, try again")


"""
Realiza un programa que lea un número impar por teclado, si el usuario no introduce un numero impar debe repetirse el proceso varias veces, haste que el proceso sea correcto
"""

print("Introduce un numero impar")
n_Impar = 0
while n_Impar % 2 == 0:
    n_Impar = int(input("Insert number odd: "))
else:
    print(f"Tu numero impar es: {n_Impar}")

"""
Realiza un program que sume todos los numeros pares del 0 hasta al 100, puedes utilizar funciones de sum() y range(), el parametro salto brinda un salto de numero

"""
# 1 sin bucle

List_n1to100 = sum(list(range(0,101,2)))
print(List_n1to100)

# suma = sum(List_n1to100)
print(f"El resultado de la suma con list y range es el siguiente: {suma}")

# #2 con bucle

n = 0 # 2,4,6,20,40,60,80,94,96,98,100 # Va servir para que haga el conteo hasta 100
suma2 = 0 # 2 + 4 + 6 + 20 + 40 + 60 + 80 + 94 + 96 + 98 + 100

while n <= 100:
    if n % 2 == 0:  
        suma2 += n
    n += 1

print(f"El resultado de la suma con el while es : {suma2}")

"""
Realiza un programa que pida al usuario cuantos numeros quiera introducir luego relizar una media aritmetica

"""
n_repeticiones = int(input("Cuantos numeros quieres introducir ? : "))
suma = 0

for r in range(n_repeticiones):
    suma += float(input("Introduce un numero: "))

print(f"Se han introducido: {n_repeticiones} numeros, el resultado de la suma es: {suma} , y el resultado de la media obtenida es de: {suma / n_repeticiones}")

"""
Realiza un programa que pida al usuario un numero entero del 0 al 9, y que mientras el numero no sea correcto se repita el proceso, luego debe comprobar si el numero se encuentra en la lista de numeros y notificarlos.
"""
numeros = [0,1,3,6,9,8,4,5,2,7]

while (True):
    n_inter = int(input("Introduce un numero entero entre el 0 al 9: "))
    if n_inter >= 0 and n_inter <= 9:
        break

if n_inter in numeros:
    print(F"El numero {n_inter} se encuentra en la lista de numeros {numeros}")
else: 
    print(F"El numero {n_inter} no se encuentra en la lista de numeros {numeros}")

"""
Utilizando range y la conversion a listas genera las siguientes listas dinamicamente
"""
# #1 Del 0 al 10

l1 = list(range(0,11))
print("Del 0 al 10")
print(l1)

# #2 Del -10 al 0

l2 = list(range(-10,1))
print("Del -10 al 0")
print(l2)

# #3 Del 0 al 20

l3 = list(range(0,21,2))
print("Del 0 al 20")
print(l3)

# #4 Numeros Impares Del -20 al 0 (-19 al -1 : Numeros Impares)

l4 = list(range(-19,0,2))
print("Del -20 al 0")
print(l4)

# #5 Del 5 al 50

l5 = list(range(5,51,5))
print("5 en 5 hasta 50")
print(l5)


"""
Dadas dos listas , debes generar un tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningun elemento en la nueva lista:
"""

lista_1 = ["h","o","l","a"," ","m","u","n","d","o"]
lista_2 = ["h","o","l","a"," ","l","u","n","a"]
lista_3 = [] # it will be ['h', 'o', 'l', 'a', ' ', 'u', 'n']

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)
print(lista_3)