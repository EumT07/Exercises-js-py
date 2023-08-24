# Exercise 1
""" 
Realiza un programa que lea 2 numros por teclado y dertemine los siguientes aspectos
    si los dos numeros son iguales
    Si los dos numeros son diferentes
    Si el primero es mayor que el segundo
    si el segundo es mayor o igual al primero

"""

# Para insertar valores se usa el metodo input
# Result

numero1 = float(input("Insert Firsth number: "))
numero2 = float(input("Insert Second number: "))

# 1
rs1 = numero1 == numero2
print(f"Son iguales ? : {rs1}")

rs2 = numero1 != numero2
print(f"Son desiguales ? : {rs2}")

rs3 = numero1 > numero2
print(f"Numero 1 es mayor a numero2 ? : {rs3}")

rs4 = numero2 >= numero1
print(f"Numero 2 es mayor o igual a numro 1? : {rs4}")

# Exercise 2

"""
Utilizando operadores logicos, determina si un string tiene en su longitud un dato mayor o igual a 3, y menor que 10:

"""

cadena = input("Inserte un string: ")

len_cadena = len(cadena)

result = len_cadena >= 3 and len_cadena < 10
print(f"El resultado es el siguiente: {result} debido a que la longitud de la cadena es de: {len_cadena}")

# Exercise 3

"""
Realiza un programa con los siguientes requerimientos
    crea una variable llamada numero magico, el valor sera el siguiente = 12345679
    recibe un valor del usuario entre el 1 y 9
    multiplica el numero de usuario por 9 en si mismo
    multiplica el numero magico, por el numero del usuario
    finalmente muestra el resultado

"""

n_magic = 12345679
n_user = int(input("Inserte un numero entre el 1 y el 9 : "))
n_user *= 9
# print(n_user)
n_magic *= n_user
print(f"El numero magico es el siguiente: {n_magic}")