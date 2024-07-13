"""
Crea una funcion llamada; Leer un numero --> leer_numero(), esta funcion tomara valores: ini, fin, mensaje. El objetivo es leer por pantalla un numero >= ini y <= fin. Ademas debe mostrar un input : enviado funcion. Luego devolvera el valor. Esta funcion debe devolver un numero, y tiene que repetirse hasta que el usuario no lo escriba bien.

-Una vez creada la funcion, crea una nueva funcion llamada generador, no recibira ningun parametro, dentro leera dos numeros con la funcion leer_numero

    1 numero: sera llamada numeros: deberas tener entre 1 y 20, ambos incluidos y se mostrara el mensaje ¿Cuantos numeros quieres generar? [1-20]
    2 numero: sera llamado modo y sera entre 1 y 3, el mensaje sera: ¿Como quieres redondear los numeros? [1]A la Alza [2]A la baja [3] normal:

-Una vez sepa los numeros a generar y como redondearlos, realiza los siguiente:
    1 Genera una lista de numeros aleatorios decimales, entre 0 y 100 con tantos numeros como el usuario haya indicado
    2 A cada uno de esos numeros deberas rendondearlos en funcion de lo que el usuario ha especificado en el modo
    3 Para cada numero muestra, durante el redondeo, el numero normal y despues del redondea
-Finalmente devolveras la lista de numeros redondeados

El objetivo de este ejercicio es paracticar la reutilizacion de codifo y los modulos randos y math

"""
#Funcion leer
import random
import math

def leer_numero(ini,fin,mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Error: Numero no valido")
        else:
            if valor >= ini and valor <= fin:
                break
    return valor


def generador():
    numeros = leer_numero(1,20,"¿Cuantos numeros quieres generar? [1-20] ")
    modo = leer_numero(1,3,"¿Como quieres redondear los numeros?:\n [1] A la alza\n [2] A la baja\n [3] Normal \n: ")

    lista = []
    for i in range(numeros):
        numero = random.uniform(0,101)
        if modo == 1:
            print(f"{numero} => {math.ceil(numero)}")
            numero = math.ceil(numero) 
        elif modo == 2:
            print(f"{numero} => {math.floor(numero)}")
            numero = math.floor(numero)
        elif modo == 3:
            print(f"{numero} => {round(numero)}")
            numero = round(numero)
        lista.append(numero)

    return lista

generador()


