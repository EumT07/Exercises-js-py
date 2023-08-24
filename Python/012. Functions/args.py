# 6 Armuments and params *args return tuple

def indeterminados_posicion(*args):
    print(args)
rl = indeterminados_posicion(5,"hola",[1,2,"b"])


#Args loops
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
        
indeterminados_posicion(5,"hola",[1,2,"b"])

#kwargs
#kw: key word
#args = argumentos 

def generarUn_Dictionario(**kwargs):
    print(kwargs)
generarUn_Dictionario(nombre="Anddres", apellido="Evan",edad=24)


def recorriendo_G_Dictionario(**kwargs):
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])
recorriendo_G_Dictionario(nombre="Eublan", apellido="Mata",edad=29)

# sumar valores en una super funcion,
# args --> todos por posicion
# kwargs --> todos con clave y valor 

def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print("Suma de todo los argmentos tipo num: es de", t)
    for kwarg in kwargs:
        print(kwarg, " ",kwargs[kwarg])

super_funcion(10,200,-1,2.34, nombre="Eublan", edad=29)
