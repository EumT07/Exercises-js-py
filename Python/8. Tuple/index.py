#Tuples are similar to list, but we can create them with (), we can change any value or modificate them

#1: Creating a tuple with ()
x = (1,2,3)
print(x)

#2: Using reserve word : Tuple
y = tuple(("a","b","c"))
print(y)

#3: if you want to creat a tuple with just one argument you need to add ","
z = ("hello",)
print(z)

#Example about tuple in real life
locations = {
    (12.32342, 23.33423): "ven",
    (1.452234, 2.32323): "col" 
}
print(locations)

#Getting the values from tuple

new_tuple = ("hello", "world",[1,2,"Value 3",4,5],"think","bye","hello")

print(new_tuple[2][2])# "Value 3"
print(new_tuple[3])# think
print(len(new_tuple))#leng: 5
print(new_tuple.count("hello"))#How many hello are there in the tuple: 2
