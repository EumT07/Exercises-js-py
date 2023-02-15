"""
String Methods
"""

# String

text1 = "Hello and 'welcome' to this new string"
text2 = "Hello, today you will learn a new \"thing\" about strings"

print(text1)
print(text2)

#routes or links : 1 \t -> don't this.
print("C:\name\pasth\thought.com")

#Add r in order to can get a good path
print(r"C:\name\pasth\thought.com")

#Join text
print("\n< < Join text > >\n")
text_A = "Hello"
text_B = "and"
text_C = "Welcome"

#1 
print(text_A,"",text_B,"",text_C)
print(text_A + " " + text_B + " " + text_C)
print("{} {} {} ".format(text_A,text_B,text_C))
print(f"{text_A} {text_B} {text_C}")# f / F


#--------------------#
#   String methods   #
#--------------------#

"""
dir(): it allows us to see a lot of methods what we can use in order to transform our strings
"""
print("\n#   String methods   #\n")

string = "Hello World"
#print(dir(string))

#Lenght 
print("Length: ", len(string))

# Methods to Transform Text

print("upper(): ",string.upper()) # HELLO WORLD
print("lower(): ",string.lower()) # hello World 
print("swapcase(): ",string.swapcase())# hELLO wORLD 

#both have the same result
print("title(): ",string.title())# Hello World
print("capitalize(): ",string.capitalize())# Hello World 

# Methods to find out if they are in Capital Letters, lowercase, if they have number inside the text, or is there is any space, they will return us a result as boolean

#--------------------#
#   if a String is   #
#--------------------#

print("\n#  if a String is  #\n")
test_text = "holas12tu758434"

#isdigit()
print("\n< isdigit >\n")
print(test_text.isdigit())# is is a digit-> false
num = "2345"
print(num.isdigit())# is a digit -> True

#isalnum()
print("\n< isalnum >\n")
print(test_text.isalnum())# alphanumeric -> True

#isalpha()
print("\n< isalpha >\n")
print("Holamundo".isalpha())#True
print("Hola Mundo".isalpha())#False, there is a space

#islower()
print("\n< islower >\n")
print("hello".islower())# True
print("Hello".islower())# False

#isupper()
print("\n< upper >\n")
print("HELLO WORLD".isupper())#True
print("hello world".isupper())#False

#Test is there is a space inside the text
print("\n< isspace >\n" )
print(" ".isspace())
print("-".isspace())