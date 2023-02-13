"""
It alow us to divide the information into two paths, 'if something happens or not'.
"""

# if
a = 3
if a == 3:
    print("They are similar")

# if - else statements
grettings = "hll"
if grettings == "Hello":
    print("They are Equals")
else:
    print("They are different")

#Little exercise
string = input("Insert number: >_")
#Changing string from input and convert into a int or float
num = int(string)
if num < 5:
    print(f"{num} is less than 5")
else:
    print(f"{num} is greater than 5")

#if - elif - else

grades = float(input("Insert grades: > "))

if grades >= 10:
    print(f"Student's Grades {grades}")
    print("Congratulations, you got 10")
elif grades >= 7:
    print(f"Student's Grades {grades}")
    print("Congratulations, you got 7")
elif grades >= 6:
    print(f"Student's Grades {grades}")
    print("you got 6, You pass it, but you nee to study more")
elif grades  >= 3 and grades <=5:
    print(f"Student's Grades {grades}")
    print("Unfortunately you need to study and take this test again..")
else:
    print(f"Student's Grades {grades}")
    print("Sorry You need to take the course again")


# if, elif and else


color = input("insert color: ")
lowercolor = color.lower()

if lowercolor == "red" :
    print(f"The color {lowercolor.capitalize()} exist")
elif lowercolor == "blue":
    print(f"The color {lowercolor.capitalize()} exist")
elif lowercolor == "yellow":
    print(f"The color {lowercolor.capitalize()} exist")
else:
    print(f"there is not any {color} inside this list")

"""
not : is not Equal
"""
x = 15
y = 40

if x > 10 and x <=20:
    print(f"{x} is greater than 2 and less or equal to 20")
if x > 12 or x < 20:
    print(f"{x} is greater than 39 and less or equal to 20")
if(not(x == y)):
    print("x is iqual y")


#Switch Python

value = 4 
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case 3:
        print("Value is 3")
    case 4:
        print("Value is 4")
    case 5:
        print("Value is 5")