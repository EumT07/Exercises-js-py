#Comparar conjuntos:

cj1 = {1,2,3}
cj2 = {3,4,5}
cj3 = {-1,99}
cj4 = {1,2,3,4,5}

#####################################################
# 1 disjunto: Si es distinto, no hay elemento comunes
#####################################################

#Disjunto o distintos--> isdisjoint()
cj1.isdisjoint(cj3)# True 
cj1.isdisjoint(cj2)# False

#############################################################
# 2 subconjunto: si se encuentra completamente dentro de otro 
#############################################################

#Subconjunto --> issubset()

cj1.issubset(cj4)#True 
#cj1 --> 1,2,3 : cj4 --> "1,2,3",4,5

cj2.issubset(cj4)#True
#cj1 --> 3,4,5 : cj4 --> 1,2,"3,4,5"

cj3.issubset(cj4)#False , nada concuerda


###############################
# 3 contenedor: si lo contiene
###############################

#Contenedor --> issuperset()

cj3.issuperset(cj4)# False, no esta contenido 
cj4.issuperset(cj1)# El contenedor cj4 contiene a cj1 # true
cj4.issuperset(cj2)# True, cj4 contiene cnjuntos de cj2 y cj1


#####################################################
# Metodos avanzados
#####################################################

# Union --> union()

#{1,2,3} {3,4,5} == {1,2,3,4,5}
cj1.union(cj2) == cj4 # True {1,2,3,4,5}
# los set no repiten, pero sin actualizarlo

# Update -> update()

cj1.update(cj2) #{1,2,3,4,5}
print(cj1)# {1,2,3,4,5} lo actualizaria.

# Saber que elemento distinto que esten en un set no esten e otro conjunto

# Diferente -> difference()
cj1.difference(cj2)# {1,2}: 1,2 son elemento del cj1 que no estan en cj2

# Different y update -> difference_update(): hara una diferencia y lo va actualizar.

cj1.difference_update(cj2)
print(cj1)#{1,2}

# intersection() : donde los conjuntos se intersectionan
# cj1 = {1,2,"3"}
# cj2 = {"3",4,5}

# Intersection
cj1.intersection(cj2)# 3 es donde es la iterseccion

# Intersection_update
cj1.intersection_update(cj2)# va actualizar a cj1 --> 3

# Diferencia simetrica: symetric_difference(), buscara la diferencia simetrica que no concuerden

cj1.symmetric_difference(cj2)# {1,2,4,5}todo los elemento no concuerdan entre ambos, eso es una diferencia simetrica