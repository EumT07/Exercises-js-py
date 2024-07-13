import random
from secrets import choice

random.random() # >= 0 y <= 1

# Un numero entre el 1 y el 10 --> numeros flotantes

random.uniform((1,10))

# Un rango entre numeros enteros

random.randrange(10) # >= 0 y <= 9

# Un rango entre numeros enteros

random.randrange(0, 101) # >= 0 y <= 100

# Un rango entre numeros enteros, contando los numeros pares

random.randrange(0, 101, 2) # >= 0 y <= 10


# rango choice

#string
c = "hola mundo"

random.choice(c)# Elegira una letra aleatoria

#lista

l = [1,2,3,4,5]
random,choice(l)# un numero alateoria 


#random.shuffle() --> desordena las lista o la cadena 

l = [1,2,3,4,5]
#random.sample(l,n) --> va traer any cantidad de numero como se le indicque. 



