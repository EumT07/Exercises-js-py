#In order to use Math Methods we need to import math module
import math

pi = 3.14 #is a float number

#PI
print(math.pi)
#euler
print(math.e)

#Round():
result_pi = round(4.5)# --> 5
result_pi = round(4.3)# --> 4

#int
print(int("23"))
print(float("12.5"))

# Round floor

math.floor(3.5)# 3

# Round ceil

math.ceil(3.2)# 4

# abs numbers

abs(10)# 10
abs(-10)# 10

# sum()

s = [2,3,4]
sum(s)# 9

# math.fsum() --> add a float number

math.fsum(s)# 9.0

# reduce decimals

math.trunc(120.345)# 120

# Power Numb

# before
2 ** 3 #8

# after
math.pow(2,3)#8

# square root

math.sqrt(9)# 3