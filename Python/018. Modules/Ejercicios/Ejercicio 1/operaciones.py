# Crear funciones: 

# Sumar 
def suma(num1,num2):
    print("Suma")
    try:
        return num1 + num2
    except TypeError:
        print("You have an error.. check your Sintaxys")
    except ZeroDivisionError:
        print("You can not make a deivision with 0..")


#Resta
def resta(num1,num2):
    print("Resta")
    try:
        return num1 - num2
    except TypeError:
        print("You have an error.. check your Sintaxys")
    except ZeroDivisionError:
        print("You can not make a deivision with 0..")



#Producto
def producto(num1,num2):
    print("Producto")
    try:
        return num1 * num2
    except TypeError:
        print("You have an error.. check your Sintaxys")
    except ZeroDivisionError:
        print("You can not make a deivision with 0..")

#Division
def dividir(num1,num2):
    print("Division")
    try:
        return num1 / num2
    except TypeError:
        print("You have an error.. check your Sintaxys")
    except ZeroDivisionError:
        print("You can not make a deivision with 0..")




