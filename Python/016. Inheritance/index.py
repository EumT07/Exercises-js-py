"""
La Herencia; capacidad de una clase heredar los atributos y metodos de otra ademas de agregar o modificar los heredados..

se conoce como superclases y subclases

Productos: Adornos alimentos libros
todos tenian: Referencia Nombre Precio y Descripcion
Alimentos: Productor y Distribuidor
Libros: Isbn y autor

"""

# Producto Clase modelo o molde
class Producto:#Classe Principal
    def __init__(self,referencia,tipo,nombre,precio,descripcion):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    def __str__(self):
        # \ : para eliminar una linea en blanco 
        return f"""\
TIPO:\t\t{self.tipo}
Nº REFERENCIA:\t{self.referencia}
NOMBRE:\t\t{self.nombre}
PRECIO:\t\t{self.precio}
DESCRIPCION:\t{self.descripcion}"""
        
#Se establece un Un producto de la clase principal.

#Herencia de una clase
class Adorno(Producto):
    pass

#Asignamos el Primer objeto con la clase Adorno
ad = Adorno(23432,"ADORNO","Taza",12,"Taza de Porcelana")
# print(ad)
# print("\n")

#Nueva clase de alimento que herede a producto.
class Alimento(Producto):
    productor = ""
    distribuidor = ""
    #  Redefinimos para agregar los nuevos atributos
    def __str__(self):
        return f"""\
TIPO:\t\t{self.tipo}
Nº REFERENCIA:\t{self.referencia}
NOMBRE:\t\t{self.nombre}
PRECIO:\t\t{self.precio}
DESCRIPCION:\t{self.descripcion}
PRODUCTOR:\t{self.productor}
DISTRIBUIDOR:\t{self.distribuidor}"""

alimento = Alimento(23445,"ALIMENTO","Harina Pan",2,"Hariana de maiz para arepas")
alimento.productor = "Hacienda Polar"
alimento.distribuidor = "Empresas POLAR S.A"
#print(alimento)

# Clase libro que herede la super clase Productor
#print("\n")
class Libro(Producto):
    isbn = ""
    autor = ""
    def __str__(self):
        return f"""\
TIPO:\t\t{self.tipo}
Nº REFERENCIA:\t{self.referencia}
NOMBRE:\t\t{self.nombre}
PRECIO:\t\t{self.precio}
DESCRIPCION:\t{self.descripcion}
ISBN:\t\t{self.isbn}
AUTOR:\t\t{self.autor}"""

li = Libro(9894,"LIBRO","La casa Grande",20,"Una casa que es grande")
li.isbn = "34434-541-9" 
li.autor = "Alberto Mata"
#print(li)

# Crear una lista 
productos = [ad, alimento]
productos.append(li)

# Recorrer
for p in productos:
    print(p,"\n")

# Recorrer y mostrar alguna referencia , siempre y cuando coincidan con todos las clases anteriores.

for p in productos:
    print(p.referencia,p.tipo,p.nombre)

#Gestionar clases; si se desea conocer algun dato, pero este no se encuentra en alguna clases, ejemplo autor, solo aplica para libros, entonces dara un error las otras clases.

# isinstance Permite comprobar si algun objeto es de tipo; ( dependiendo de la clase )

for p in productos:
    if(isinstance(p, Adorno)):
        print(p.referencia,p.nombre,p.tipo)
    elif(isinstance(p, Alimento)):
        print(p.distribuidor,p.tipo)
    elif(isinstance(p, Libro)):
        print(p.autor,p.tipo,p.isbn)

#Realizar modificacion de los atributos 

def rebajar_producto(p,rebaja):
    """
    Va devolver un producto con una rebaja en % de su precio
    """
    p.precio = p.precio - (p.precio/100 * rebaja)
    return p

alimento_rebajado = rebajar_producto(alimento, 20)
#print(alimento_rebajado)
#print(alimento)# EL precio se actualizo por la herencia

# No se puede copiar a menos que utilicemos un metodo, mientras siempre va a obtener el mismo resultado actualizado 
from copy import copy

copia_ad = copy(li)
copia_ad.precio = 34

# print(copia_ad) #Permite copiar , entonces podriamos modificar este obejto, pero el original no tendria ninguna refrencia 
# print(li)

"""
Poliformia: es la propiedad de la herencia en que objetos de distintas subclases pueden responder una misma accion, todas las clases son poliformicas por defectos
"""

#Herencia multiples

class A:
    def __init__(self):
        print("Soy clase A")
    def a(self):
        print("Este metodo se hereda de A")
class B:
    def __init__(self):
        print("Soy clase B")
    def b(self):
        print("Este metodo se hereda de B")
class C(B,A):
    def c(self):
        print("Este metodo es unico de C")

c = C()#Soy clase B --> va primero el que vaya deacuerdo a la posicion que se envian

c.a()#Este metodo se hereda de A
c.b()#Este metodo se hereda de B
c.c()#Este metodo se hereda de C