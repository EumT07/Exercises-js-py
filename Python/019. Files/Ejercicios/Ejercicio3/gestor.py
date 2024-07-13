"""
Utilizando como base el ejercicio de los personajes que hicmos, en este ejercicio tendrás que crear un gerstor de personajes(gestor.py), para añadir y borrar la informacion de los siguientes personajes:

            Vida | Ataque | Defensa | Alcance
Caballero      4 |      2 |       4 |       2
Guerrero       2 |      4 |       2 |       4
Arquero        2 |      4 |       1 |       8


Deberas hacer uso del modulo pickle y todos los cambios que realices se iran guardando en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistiran 

    .Crea dos clases, uno Personas y otra Gestor

    .La clase Personaje deberá permitir crear un personaje con el nombreUQue será la clase), y sus propiedades de vida, ataque, defensa y alncance (que deben ser numeros enteros positivos mayor que cero obligatoriamente)

    .Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes, mostrarlos, y borralos (a Partir de su nombre por ejemplo)(tendrás que pensar una forma de hacerlo),además de los metodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberian ejecutar automaticamente.
    
    .En caso de que el personaje ya exista en el gestor entonces no se creará.


Una vez lo tengas listo realiza las siguientes pruebas en tu codigo:

    .Crea los personajes de la tabla anterior y añadelos al gestor
    .Muestra los personajes del gestor
    .Borra al Arquero
    .Muestra de nuevo el gestor



"""

import pickle

class Personajes:
    def __init__(self,nombre,vida,ataque,defensa,alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    def __str__(self):
        return f"{self.nombre} => {self.vida} vida, {self.ataque} ataque, {self.defensa} defensa, {self.alcance} alcance"

class Gestor:
    personajes = [] #Atributo

    def __init__(self):
        self.cargar()

    def agregar(self,pers):
        for personajeTemp in self.personajes:
            if personajeTemp.nombre == pers.nombre:
                return
        self.personajes.append(pers)
        self.guardar()
    
    def borrar(self,nombre):
        for personajeTemp in self.personajes:
            if personajeTemp.nombre == nombre:
                self.personajes.remove(personajeTemp)
                self.guardar()
                print(f"\n Personaje {nombre} borrado")

    def mostrar(self):
        if len(self.personajes) == 0:
            print("El Gestor esta vacio")
        else:
            for p in self.personajes:
                print(f"Pelicula: {p}")
                
    def cargar(self):
        fichero = open("personajes.pckl","ab+")
        #ab+ : modo de lectura, y escritura
        fichero.seek(0)#Colocar 0 para que siempre inici en idx 0
        #Comprobar en el catalogo las peliculuas que hay
        try:
           self.personajes = pickle.load(fichero)
        except:
            # print("El fichero está vacío")
            pass 
        finally:
            print(f"Se han cargado {len(self.personajes)} personajes")

    def guardar(self):
        fichero = open("personajes.pckl","wb")
        pickle.dump(self.personajes, fichero)
        

g = Gestor()
# g.mostrar()

# g.agregar(Personajes("Caballero",4,2,4,2))
# g.agregar(Personajes("Guerrero",2,4,2,4))
# g.agregar(Personajes("Solteldo",2,4,1,8))

# g.borrar("Arquero")
g.borrar("Solteldo")
g.mostrar()



















































