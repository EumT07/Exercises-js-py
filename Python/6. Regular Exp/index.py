import re

"""
Regular Expresion I
"""
text = "There is a bird in front of the window"

#Search
print(re.search("bird", text))#<re.Match object; span=(11, 15), match='bird'>

#Using conditional stament
#If there is not any word it return none
found_it = re.search("window",text)

if found_it is not None:
    print("This word Exists")
else:
    print("This word doesn't exist")

#searching the word and get the position in the text

#start, ned, span, string
print(found_it.start())#32
print(found_it.end())#38
print(found_it.span())#(32,38)
print(found_it.string)# There is a bird in front of the window

#match
text2 = "Hello world"
print(re.match("Hello",text2))

#Split

text3 = "Today is a good day"
result = re.split(" ", text3)
print("Split: ", result) #get a new list

# Sub
result_sub = re.sub("good","bad",text3)
print("Sub: ",result_sub)

#how many times we can find a word into a text

text4 = "hello hello world hello hola world" 
result_findall = re.findall("hello", text4)
print("Findall: ", result_findall)

#like a tunel
result_findall_tunel = re.findall("(hello|hola)",text4)
print("Find all Tunel: ",result_findall_tunel)

"""
Regular Expresion II
"""
print("\nRegular Expression II\n")
text5 = "hlp help heelp heeelp heeeeeelp"

def searchText(patterns, text):
    for pattern in patterns:
        print(re.findall(pattern,text))

# patterns = ["hlp","help","heelp"]
# patterns = ["he","he*", "he*lp"]#How many e you will find
# patterns = ["he*","he+", "he?","he?lp"]
patterns = ["he{1}lp","he{2}lp","he{1,6}lp"]#Hrange

searchText(patterns,text5)

"""
Regular Expresion III
"""
print("\nRegular Expression III\n")
# text6 = "hala hela hila hola hula"
# text6 = "haala heeela hiiila hoooola huula"
text6 = "hola Hola H0la h0la" #Range

# patterns2 = ["h[ou]la","h[aei]la"]
# patterns2 = ["h[ou]la","h[aei]*la","h[ou]{2,4}la" ]
# patterns2 = ["h[o]la","h[^o]la" ]

# Range [A-Z],[a-z],[0-9]
patterns2 = ["h[a-z]la","h[0-9]la", "[A-z][0-9]la" ]

searchText(patterns2,text6)

