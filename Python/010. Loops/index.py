"""
Loops: Permite recorrer las colecciones; listas, tuplas, set o conjuntos, asi como los diccionarios, permite recorrer numeros, es muy usado para conteos regresivos, se utiliza el while y el for, asi como los metodos break y continue.

"""

## While

c1 = 0
while c1 <= 3:
    # print("Value before add 1: ", c)
    c1 +=1
    print("Value after: ", c1)
else:
    print(f"End : {c1}")

# While with break, continue

c2 = 0
while c2 <= 10:
    c2 += 1
    if c2 == 4:
        # print(f"Break the loops: value c2 = {c2}")
        # break
        print(F"Continue the loops")
        continue
    print(c2)
else:
    print(f"End : {c2}")

# With list

food = ["arepa", "tacos","empanadas"]

i = 0
while i < len(food):
    print(food[i])
    i += 1

#################### For #####################

# List-string
foods = ["apples", "bread", "cheese", "milk"]

print(foods)
print(foods[3])#milk

#for in

for food in foods:
    print(food)

#for in with break and continue
for food in foods:
    if food == "cheese":
        print("You need to buy it because it's tasty")
        # break
        continue
    print(food)

#  from 10 to 100
numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    number *= 10
    print(number)

#Creating an external index
i = 0
for number in numbers:
    numbers[i] *= 10
    i += 1
    print(numbers)


## enumerate ##

""" enumerate(iterable, start=0)
iterable - a sequence, an iterator, or objects that supports iteration
start – is the position in the iterator from where the counting starts.
Default is 0.
"""
days= { 'Mon', 'Tue', 'Wed','Thu'}
enum_days = enumerate(days)
# print(type(enum_days))# class enumerate

# converting it to alist
# print(list(enum_days))
#[(0, 'Tue'), (1, 'Thu'), (2, 'Mon'), (3, 'Wed')]


"""
Range: it take 3 parameters
1 inital number
2 end number
3 salt --> it allow us to jump into number: even or odd
"""

for number in range(1,8):
    print(number)

for i in range(10):
    print(i)

print(list(range(0,101)))

#Salt 
# even numer
print(list(range(0,101,2)))

# odd number 
print(list(range(1,101,2)))

# 20 in 20 
print(list(range(0,101,20)))
