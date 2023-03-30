"""
Class: es como un molde que permite crear objetos (instancias de clases, hace referencia a la memoria del ordenador solo cuando el programa esta en marcha, se crea apartir de una clase)

type() --> muestra el tipo de dato

"""

class Icecream:
    pass

cocoIcecream = Icecream()
type(cocoIcecream)# __main__.Galleta

#Creating a new class

class Car:
    new = True
    def __init__(self,model,color,tires):
        self.model = model
        self.color = color
        self.tires = tires
        print(f"model: {model} , color: {color} tires: {tires}")

    def usado(self):
        self.new = False

    def precio(self):
        if(self.new):
            print("This carr is new")
        else:
            print("This car is old")

car1 = Car("mustang","white",4)

print(car1)
print("-----")
car1.usado()
car1.precio()
print("-----")

#Methods: Init, del, str,len

class Lesson:
    #Class Constructor
    def __init__(self,title,duration,start):
        self.title = title
        self.duration = duration
        self.start = start
        print(f"Lesson: {self.title}")

    #Delete class
    def __def__(self):
        return f"{self.title} was deleted from our class' list"
    
    #string 
    def __str__(self):
        return f"{self.title} will start at {self.start} am and has a duration {self.duration} minutes"
    
    #length
    def __len__(self):
        return self.duration

english = Lesson("Verbo to be", 45,8)

print(english)

#Object in object

class Movie:
    #Constructor de clase
    def __init__(self, title, duration, release):
        self.title = title
        self.duration = duration
        self.release = release
        print(f"Film: {self.title}")
    
    #Redefiniendo el metodo string
    def __str__(self):
        return f"Movie: {self.title} Year: ({self.release}) duration {self.duration} minutes"
  
class Catalogue:
    movies = [] #Atributo
    def __init__(self,movies=[]):
        self.movies = movies
    def add(self,movie):
        self.movies.append(movie)
    def show(self):
        for p in self.movies:
            print(p)

movie1 = Movie("La monja",202,2018)
movie2 = Movie("El cuervo",150,1992)
print(movie1)
print(movie2)

c = Catalogue([movie1])
c.show()
c.add(movie2)
c.add(Movie("Capitan rock",45,2015))
c.add(Movie ("Lluvia",85,2008))
c.show()