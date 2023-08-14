"""
POO : Programacion rientada a objetos, paradigma, soluciones de problemas.

"""
#Programcion estructurada
clientes = [
    {"Nombre":"Evans","Apellido":"smith", "ci":41254784},
    {"Nombre":"Elizabet","Apellido":"tailor", "ci":4521478}
]
#Funcion para buscar cliente en la base de datos
ci = int(input("Inserte CI: "))
def buscar_cliente(clientes,ci):
    for cliente in clientes:
        if (ci == cliente["ci"]):
            print(f'Se encontro a la siguiente persona en nuestra base de datos: {cliente["Nombre"]} {cliente["Apellido"]} {cliente["ci"]}')
            return
    print("Cliente no se encuentra en nuestra base de dato")
buscar_cliente(clientes,ci)
#Borrar de la base de datos
ci = int(input("Inserte CI del usuario que desea eliminar: "))
def borrar_cliente(clientes, ci):
    for i,cliente in enumerate(clientes):
        if (ci == cliente["ci"]):
            del(clientes[i])
            print(str(cliente), "> Fue borrado de la base de dato")
            return
    print("Cliente no se encuentra en nuestra base de dato")
borrar_cliente(clientes,ci)


"""
Programacion orientada a objetos

"""

class Cliente:
    #Costructor
    #Self seria el this en este caso
    def __init__(self,ci,nombre,apellido):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
    #Metodos para poder imprimir 
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes
    def buscar_cliente(self, ci=None):
        #Mostrar
        for c in self.clientes:
            if c.ci == ci: 
                print(c)
                return
        print("cliente no encontrado")
    def borrar_cliente(self, ci=None):
        #Borrar
        for i,c in enumerate(self.clientes):
            if c.ci == ci:
                del(self.clientes[i])
                print(str(c), "> Borrado")
                return
        print("Cliente no encontrado")
    def  mostrar(self):
        #Muestra una lista de clientes
        for c in self.clientes:
            print(c)

cliente1 = Cliente(4125472,"Luke","Cage")
cliente2 = Cliente(1425783,"Elizabeth", "Taylor")
# print(str(cliente1))
# print(str(cliente2))

empresa = Empresa(clientes=[cliente1,cliente2])
empresa.mostrar()# Va mostrar los dos clientes
empresa.buscar_cliente(4125472)#
empresa.buscar_cliente(ci=2145874)# No encontrado
empresa.borrar_cliente(1425783)# 
empresa.mostrar()#
