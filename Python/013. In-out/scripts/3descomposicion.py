import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1]) # 3647
    if numero < 0 or numero > 9999:  
        print("There is an Error")
        print("You must write: descomposicion.py \"[0-9999]\" ")
    else: # [0 --> 3647 <-- 9999]
        #Logic
        cadena = str(numero) #3647
        leng_cadena = len(cadena) # length --> 4 

        for i in range(leng_cadena): # --> range of 4
            print(f"{int(cadena[leng_cadena - 1 - i])* 10 ** i:04d}")
            #7 * 1 = 7 + los rellenos de 0 = 0007
            #4 * 10 = 40 + los rellenos de 0 = 0040
            #6 * 100 = 600 + los rellenos de 0 = 0600
            #3 * 1000 = 3000 + los rellenos de 0 = 3000

            #resultado final : 3647
else:
    print("There is err")
    print("You must write: descomposicion.py \"[0-9999]\" ")


# definicion

"""
            f --> format
            {
                int(
                    cadena --> # 3647 leng_cadena --> # 4 - 1
                )-> Interger Number
                * 10 **(elevado) 1  --> 
                1ra itr = 1, 
                2da itr = 10, 
                3ra itr = 100, 
                4ta itr = 1000
            }
 """