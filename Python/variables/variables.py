#Keyword and reserved words
import keyword
# print(keyword.kwlist)

#Data Types

#String
# print("Hello world")
# print('Hello world')
# print("""Hello world""") #Multy lines

#Numbers
# print(23) #Int
# print(3.14) #float

#Boolean
# print(True) # -> 0
# print(False) # -> 1

#Variables

name = "Miguelito"
last_Name = "Guillermo"
age = 30
DNI = 4543234

#1 
print("name: ", name)
print("last_Name: ", last_Name)
print("age: ", age)
print("DNI: ", DNI)

#2 Concat
print("Hello, my name is: " + name + " last name is: " + last_Name)
print('My age: ' + str(age) + " My DN: " + str(DNI))

#3:
# #format -> A
print("Hello, my name is {} and my lastName {}, I'm {} and this is my DNI: {}".format(name, last_Name,age, DNI))

# Format -> B f or F
print(f"Hello, my name is {name} and my lastName {last_Name}, I'm {age} and this is my DNI: {DNI}")