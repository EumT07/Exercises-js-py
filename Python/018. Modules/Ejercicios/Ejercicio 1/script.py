"""
Crea el siguiente modulo:

Operaciones: Suma, resta, producto y division. --> devolver resultado

Deberas tratar los errores de manera manual:

    typerr: en caso de que se envies valores no numericos
    zerodivisionerr: en caso de division con el numero cero

Una vez creado el modulo, crea un script calculos.py en el mismo directorioa en el que deberas importar el mopdulo y realiza las siguientes instrucciones. Observa si el comportamiento es el esperado.

From operaciones import

a, b, c,d = 810,5,0, HOLA


"""

from operaciones import *

a, b, c , d = (10, 5, 0, "hola")

print(f"{a} + {b} = {suma(a,b)}")
print(f"{b} - {d} = {resta(b,d)}")
print(f"{b} % {b} = {producto(b,b)}")
print(f"{a} / {c} = {dividir(a,c)}")