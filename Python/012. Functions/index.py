# Basic Function

#A

def hello():
    print("Hello")
hello()

#B
def multiply_5():
    for i in range(11):
        print(f"5 * {i} = {i * 5}")
multiply_5()

#C varible scope

def scope():
    n = 23
    print(n)# N is inside the functions

scope()
# print(n)# N doesn't exit outside the function

m = "hello"
def scope2():
    print(m)

scope2()# M is outside the function, so you can use it in both way

# Function with return
def sayBye():
    return "Bye"
bye = sayBye()
print(bye)

#return using indix or slicing

def list():
    return [1,2,3,4,5]

num = list()[:3] # bad
num2 = list()[2:4] # bad

num3 = list() # Good

print(num)
print(num2)
print(num3[-1])# Better than others

def user():
    return "Alex", "smith", 40
userDNI = user()
print(userDNI)

name, lastName, age = user()
print(f"""\n
# Name: {name}
# Last Name: {lastName}
# Age: {age}
# \n""")

# 3 Arguments and Params

def suma(n1,n2): #values (Params)
    return n1 + n2
result = suma(10,20)#Values (Arguments)
print(result)

# 4 Arguments and params by default

#Params by default
def substr(a, b=4):
    return a - b 
result2 = substr(1)
print(result2)

#Arguments by default
def multiply(a,b):
    print("a: ", + a)
    print("b: ", + b)
    return a * b
c = multiply(b= 4, a=5)
print(c)

# None argumentos
def divide(a=None,b=None):
    if a == None or b == None:
        # print("Error, Debes enviar dos arg  a la funcion")
        return
    else:
        return a / b
divide()# return print()
rsl = divide(100,5)
print(rsl)

# More than two arguments: Return tuple

def words(param1,param2, *othersParams):
    words = [param1,param2,othersParams]
    for w in words:
        print(f"result: {w}")

words("hola","Buenos","Dias","Tarde","Noches","Madrugada")
    
"""
result: hola
result: Buenos
result: ('Dias', 'Tarde', 'Noches', 'Madrugada')--> tupla
"""

# 5 

# pass by value: 
def doble_value(numero):
    numero*=2
n = 10
print(doble_value(n))
print(n) # No toma referencia

# pass by reference: Collections, list, dictionary, tuples, set

def dble(numeros):
    for i,n, in enumerate(numeros):
        numeros[i] *= 2
# dble(4)
ns = [10,50,100]
dble(ns)
print(ns)  #Take reference

# Other way to pass valyes by rerencen

def new_value(number):
    return number * 2
n = 10
n = new_value(n)
print(n)

# copiar en este caso una lista -referencia

def dble(numbers):
    for i,n, in enumerate(numbers):
        numbers[i] *= 2

ns = [20,3,45,60]
dble(ns[:]) # Copy the value and avoid the value will be modified
print(ns)


# 7 recursividad

def cuenta_regresiva(n):
    n -= 1
    if n > 0:
        print(n)
        cuenta_regresiva(n)
    else:
        print("Boooommmm!!! you are die")
    print("Fin de la funcion", n)
cuenta_regresiva(3)


#recursividad factorial
def factorial(num):
    print("Valor inicial", num)
    if num > 1:
        num = num* factorial(num -1)
    print("Valor final -->", num)
    return num # return directamente para devolver el valor de num
factorial(3)

#Funcion lambda

rest = lambda number1, number2: number1 + number2
y = rest(25,4)
print(f"Resultado de la resta fue: {y}")

sumLambda = lambda num: num * 2
print(sumLambda(4))