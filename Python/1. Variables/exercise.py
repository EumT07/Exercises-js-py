"""
Get even and odd number

"""
n = 0
while n < 11:
    if(n % 2 == 0):
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
    n += 1

"""
slicing 
"""

name = "Manuela"
new_name = name[:-1]

# print(name)
# print(new_name)

"""
Calculo de la media Media, es la suma de todos divivido entre el numero de participantes.
Nota: debe dar 6

"""

n1 = 9
n2 = 3
n3 = 6

media = (n1 + n2 + n3) / 3

# print(f"La media es de : {media}")

"""
Modificar el ultimo elemento de cada suma dentro de la lista, donde sea erronea, y aplicar el method sum(), para hacer una suma por cada lista, y luego una suma general.
"""

matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]
# Primera forma simple y basica

matriz[1][-1] = [6]
matriz[3][-1] = [12]

#segunda forma con slincing [:] and sum()

matriz[1][-1] = sum (matriz[1][:-1]) #2+2+2 = 6
matriz[3][-1] = sum (matriz[3][:-1]) # 4+4+4 = 12
# print(matriz)

# Sum total
suma = sum(matriz[1][:-1])

# print(matriz)

"""
Formatear la siguiente cadena de texto, extraer el nombre y la calificacion y concatenarla e imprimirla

"""

cadena = "zereP nauJ,01"

turn_cadena = cadena[::-1]
print(cadena)
print(turn_cadena)

# Aplicando dos forma de concatenar

print(turn_cadena[3:] + " " + "Ha sacada un" + " " + turn_cadena[:2] + " " + "de nota")# normal

print(f"{turn_cadena[3:]}\n Ha sacado un {turn_cadena[:2]} de nota\n Gracias..!!")# Format --> f-F