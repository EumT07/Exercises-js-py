"""
Localiza el error en el siguiente bloque de codigo, crea una excepion para evitar que el programa se bloquee y explique al usuario la cause del problema
resultado 10/0

"""

num = float(input("Introduce un numero "))

try:
    num / 0
except ZeroDivisionError:
    print("Hubo un error, no se puede dividir")


"""
Localiza el error

"""
lista = [1,2,3,4,5]

try:
    print(lista[10])
except IndexError:
    print(f"No hay ningun valor con ese indice, introduce un valor mayor a 0 y menor que la longitud de la lista {len(lista)}")

"""
Localiza el siguiente error:

"""

alumnos = {"alum1":"Eublan","alumn2":"Violeta"}

try: 
    alumnos["alum3"]
except KeyError:
    print("No hay ningu alumno numero 3")


"""
localiza el siguiente error

"""

try:
    resultado = 15 + "20"
except TypeError:
    print("Error..!! solo es posible sumar dos datos del mismo tipo, cambian ya sea numeros a string o string a numeros")


""""
Realiza una funcion agregar_una_vez() que reciba una lista y un elemento, la funcion debe añadir el elemento al final de la lista, con la condicion de no repetir. ADemas si este elemento si este elemento se encuentra en la lista debe arrojar o mostrar la exception, y mostrar el siguiente mensaje:

        Error: Imposible añadir elementos duplicados => [Elemento].
        
"""

elementos = [1,5,-2]

def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
    except ValueError:
        print(f"Error..!! Imposible añadir duplicados => {el}" )

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(elementos)