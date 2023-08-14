#Search into the text

string = "You must do your homework, the more you study the more you learn"

#Startwith()
print("startsWith: ",string.startswith("homework"))#False
print("startsWith: ",string.startswith("You"))#True

#endswith()
print("endaswith: ",string.endswith("the"))#False
print("endaswith: ",string.endswith("learn"))#True

string2 = "Miguelito"

print(string2)
print(string2.startswith("M"))
print(string2.endswith("l"))

#rfind()
print(string2.rfind("i"))#get the last one, and re turn the index

#find()
print(string2.find("e"))#get the First one, and re turn the index

#strip() : to delete any space
string3 = " hello .  "

print(string3.strip())#to delete any space
print(string3.lstrip())#to delete left space
print(string3.rstrip())#to delete right space


#brackets
word = "Python"
print("Index 0 : ", word[0])#P
print("Index 4 : ", word[4])#o


#Slicing : [start:end]
print("slincing: ", word[2:-1])#tho
# Py, cut and extract the entered range
# Negative number can be used according to the number of characters found

#Change a letter
word = "N" + word[1:]
print("Change - from 'Python' to this: ", word)

#split: transfor a string into an array or list
greetings = "Hello world and welcome"
saying = "the-more-you-read-the-more-you-learn"

print(greetings.split())#['Hello', 'world', 'and', 'welcome']
print(greetings.split()[3])# and
print(greetings.split(" , "))# nothing happened : ['Hello world and welcome']
print(saying.rsplit("-"))# ['the', 'more', 'you', 'read', 'the', 'more', 'you', 'learn']

#Join
result = ",".join("Hello world")
print(result)#H,e,l,l,o, ,w,o,r,l,d

#replace()
food = "I would like to eat pizza"
print("replace('pizza','Hot dog'): ",food.replace("pizza","hot dog"))

rst = "Hello hello hello my friends".replace(" hello","",2)
print(rst)
