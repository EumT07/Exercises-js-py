import pickle

class Pelicula:
    #Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f"Se ha filamado: {self.titulo}")
    
    #Redefiniendo el metodo string
    def __str__(self):
        return f"Pelicula: {self.titulo} Año: ({self.lanzamiento}) duracion {self.duracion} minutos"
  
class Catalogo:
    peliculas = [] #Atributo

    #Inicio del fichero
    def __init__(self):
        self.cargar()

    def agregar(self,peli):
        self.peliculas.append(peli)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("Esta vacio el Catalago")
        else:
            for p in self.peliculas:
                print(f"Pelicula: {p}")
                
    def cargar(self):
        fichero = open("catalogo.pckl","ab+")
        #ab+ : modo de lectura, y escritura
        fichero.seek(0)#Colocar 0 para que siempre inici en idx 0
        #Comprobar en el catalogo las peliculuas que hay
        try:
           self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print(f"Se han cargado {len(self.peliculas)} peliculas")

    def guardar(self):
        fichero = open("catalogo.pckl","wb")
        pickle.dump(self.peliculas, fichero)
        
    #Destrcutor de la clase
    def __del__(self):
        self.guardar()#Automatico


c = Catalogo()
# pelicula1 = Pelicula("La alianza Zombie",150,2008)
# pelicula2 = Pelicula("La abeja pinchin",23,2017)
# pelicula3 = Pelicula("Sinfonia Palpitante",56,2016)
# pelicula4 = Pelicula("Tarzan",140,2010)
# pelicula5 = Pelicula("La pluma del capitan",80,2007)

# c.agregar(pelicula1)
# c.agregar(pelicula2)
# c.agregar(pelicula3)
# c.agregar(pelicula4)
# c.agregar(pelicula5)

# c.mostrar()
c.cargar
del(c)



