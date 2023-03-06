"""
Conjunto --> son colecciones desordenada, cuando las iniciamos podemos inicializarlas de manera desordenada u ordenadas, pero cuando se imprimen se pueden ordenan o no, pero si agregas nuevamente un elemento, va a asignarles valores o posiciones desordenados. 

"""

colors = {"red","white","black","blue","red"}
print(colors)#{'blue', 'white', 'violet', 'black', 'red'}

#in
print("red" in colors)# True
print("yellow" in colors)# False

#add element
colors.add("violet")
print(colors)

#romove 
colors.remove("red")
print(colors)

# clear
colors.clear()#Limpiar todo el conjunto
print(colors)

# conjunto = set()
conjunto = {2,4,1,5,7,9,8,6,0,3}

#add
conjunto.add("H")
conjunto.add("A")
conjunto.add("z")
conjunto.add("t")
print(conjunto)

# It can not have two o more repeated values
test = {"A","A","A"}
print(test)

#in 
grupo = {"Hector", "Miguel", "Andrea"}

find_name1 = "Hector" in grupo
find_name2 = "Luis" in grupo

print(f"1: {find_name1} y 2: {find_name2}")


#discard(): permite descartar un elmento apartir de un idice "Eliminar"
grupo.discard("Miguel")# {"Hector", "Andrea"}

#Set

# List
l = [1,2,3,4,5,5,4,3,2,1]
print("List: ",l)

c = set(l)#Conjunto / set
print("Conjunto: ",c)

#List
l2 = list(c)
print("List nuevamente: ",l2)

#Copy()
c1 = {1,2,3}

c2 = c1.copy()
print(c2)#{1,2,3}