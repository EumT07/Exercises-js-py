"""
Excepciones/Exceptions --> bloque que permite continuar si el flujo ocurre un error
"""
# n = float(input("Insert a number: "))
# # n = input("Introduce un numero: ") #Error

# m = 4
# print(f"number = {n} /  {m} = {n/m}")

# try and except

try:
    # n = float(input("Insert a number: "))
    n = input("Insert a number:: ") #Error
    m = 4
    print(f" num = {n} / m {m} = {n/m}")
except:
    print("There is an error, try again") 

# Exceptions: While 

while (True):
    try:
        n = float(input("Insert a number: "))
        m = 4
        print(f" num = {n} / {m} = {n/m}")
        break #brean interacion si todo sale bien
    except:
        print("There is an error, try again")


# Exceptions: While / else 

while (True):
    try:
        n = float(input("Insert a number: "))
        m = 4
        print(f"num = {n} / m {m} = {n/m}")
    except:
        print("there is an errot, try again")
    else:
        print("Great")
        break


# Exceptions: While / else / finnaly 

while(True):
    try:
        n = float(input("Insert num: "))
        m = 4
        print(f"num = {n} /  {m} = {n/m}")
    except:
        print("There is an error, Try again: ")
    else:
        print("Great..!!")
        break
    finally:
        print("End..!!")

# Exception: Errors
 
#1
try:
    n = input("insert a number: ")
    result = 5 / n
    print("result: ", result)
except Exception as e:#Name of error
    print(type(e).__name__)


# 2
#chains

try:
    n = float(input("insert a number: "))
    # n = input("inserta un numero: ")
    r = 5/n
    print(r)
except TypeError:
    print("We can not divide this")
except ValueError:
    print("Insert a number not a string")
except ZeroDivisionError:
    print("You can not divide in zer0")
except Exception as e:
    print(type(e).__name__)


# Invocacion de excepciones
def mi_funcion(algo=None):
    try:
        if algo is None:# is
            raise ValueError("Err..!! value is none")
    except ValueError:
        print("Err..!values is an error from exception")

#raise : invocar un error
mi_funcion()