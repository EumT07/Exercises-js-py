# Part I

# import sys
# texto = sys.argv[1]
# repeticiones = int(sys.argv[2])
# for r in range(repeticiones):
#     print(texto)


import sys
if len(sys.argv) == 3:
    text = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(text)
else:
    print("There is a Err")
    print("You must write something like this: python pythonscript.py \"Hola\" 5 ")