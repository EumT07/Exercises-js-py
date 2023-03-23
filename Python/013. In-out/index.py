"""
In: Entrada -> input()
out: Salida -> print()
"""

#Insert a number

float_number = float(input("insert a float number: "))
print(float_number)

# List

food = []
print("Food list: ")
for x in range(3):
    food.append(input("Insert a food name: "))
print(food)
# Recorriendo Valores
for value in food:
    print(value)

# Salidas / out

text = "Hello and welcome"
name = input("Tell me your name: ")
age = input("How old are you?: ")
place = input("Where do you live? ")

#Concatenacion con f/F
oracion = f"{text}, Sr {name} you are {age} years old, and you live in {place}"
print(oracion)

#https://queirozf.com/entries/python-number-formatting-examples


