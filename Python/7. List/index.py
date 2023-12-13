#list
print("\n List \n")
data_list = [1,"a","Hello",True,False,[1,2,3,4,5]]
string_list = ["Hello", "world"]
number_list = [1,2,3,4,5,6]

print(data_list)
print(string_list)
print(number_list)

#Range
rangeList = list(range(1,11))# 1 to 10
print(rangeList)

#in: Check if a value is in an list or not.
animal_List = ["leon", "zebra","tiger","dog"]

print("cat" in animal_List)#False
print("zebra" in animal_List)#True

#Getting an element from the list. 
print(data_list[2])#Hello
print(string_list[1])#world
print(animal_List[3])#dog

#List Methods: append, extend, insert, pop, remove, sort
print("\n List Methods \n")
verbs_to = ["do", "have", "drink","still"]
print("Verbs List: ",verbs_to)

#adding a new element into de list

#append: it allows us to insert just one argument
verbs_to.append("cook")
print("Verbs List [append()]: ",verbs_to)

#extend: it allows us to insert more than one arguments
verbs_to.extend(["make","hide","type"])
print("Verbs List [extend()]: ",verbs_to)

#Adding a new element but inserting the position
#1 index
#2 element that you will add
verbs_to.insert(3,"watch")
print("Verbs List [insert()]: ",verbs_to)

# add new elemet at the end of the list
verbs_to.insert(len(verbs_to),"wash")
print("Verbs List [insert(len())]: ",verbs_to)

#Delete an element from the list
verbs_to.pop()#It will delete the last one by default
verbs_to.pop(3)#It will delete the last one by default
print("Verbs List [pop(),pop(index)]: ",verbs_to)

#Remove and espesific element
verbs_to.remove("have")
print("Verbs List [remove()]: ",verbs_to)

#Sort
verbs_to.sort()
print("Verbs List [sort()]: ",verbs_to)

#Sorted
num_list = [2,8,5,3,1,4,9,7,6]
print("Normal num List(): ", num_list)
print("Sorted List(): ", sorted(num_list))
print("Sorted List(reverse=False): ", sorted(num_list,reverse=False))
print("Sorted List(reverse=True): ", sorted(num_list,reverse=True))

print("\n deque, FIFO: First in First Out \n")

"""
Pilas o stacks : Añadir o sacar , ultimo en entrar primero en salir, 
* fifo : First in first out
* lifo : last in first out
"""

pila = [1,2,3]
pila.append(4) # --> 4 in [1,2,3,4]
pila.append(5) #--> 5 in [1,2,3,4,5]
print("Se ha agregado dos elementos, primero se agrego el 4 y luego el 5")
print(pila)
print("Ahora se eliminaran los elemento, primero el 5, ya que fue este el ultimo que se agrego, y sera el primero en salir") 
pila.pop() #5 out [1,2,3,4]
pila.pop() #4 out [1,2,3]
print(pila) # [1,2,3]

"""
Importando deque
"""

"""
pop(): --> Va eliminar por la derecha
popleft(): --> Va eliminar por la izquierda

"""

from collections import deque

cola = deque(["Hector", "Maria", "Andrea"])
print("Se agregaran dos nuevos nombres, Luis y guillermo")
cola.append("Luis") # Luis in ["Hector", "Maria", "Andrea", "Luis"]
cola.append("Guillermo")# Guillermo in ["Hector", "Maria", "Andrea", "Luis", Guillermo]
print(cola) # ["Hector", "Maria", "Andrea", "Luis", "Guillermo"]
print("Ahora se procede a mostrar el ejemplo en funcionamiento, firts in first out")
cola.popleft()# Hector out ["Maria", "Andrea", "Luis", "Guillermo"]
cola.popleft()# Maria out ["Andrea", "Luis", "Guillermo"]
cola.popleft()# Andrea out ["Luis", "Guillermo"]
print(cola)# ["Luis", "Guillermo"]
# Primero entraron a la cola hector, maria y andrea, y luego proceden a salir primeros, de acuerdo a su orden de entrada, first in first out. 
