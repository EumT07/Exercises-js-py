import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas >9:
        print("Row and colum are wrong")
        print("Example --> Tabla.py [1-9] [1-9]")
    else:
    #Logic
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" h ", end ="")
else:
    print("There is an Error")
    print("Example --> Tabla.py [1-9] [1-9]")