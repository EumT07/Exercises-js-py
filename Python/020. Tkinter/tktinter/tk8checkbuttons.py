from tkinter import *
from turtle import left

#Funciones
def seleccionar():
    message = ""
    if(milk.get()):
        message += "With milk"
    else:
        message += "Without milk"
    if(sugar.get()):
        message += " With sugar"
    else:
        message += " Without sugar"
    monitor.config(text=f"I would like my Coffee: {message}")

#Raiz
root = Tk()
root.title("CoffeLove")
root.config(bd=20)
root.iconbitmap("starbuck.ico")
root.resizable(0,0)


#Variables a elegir
milk = IntVar() # 1 = Si / 0 = No
sugar = IntVar() # 1 = Si / 0 = No


#Colocar image
imagen = PhotoImage(file="cafe.gif")
#Insertamos la imagen dentro de un frame
Label(root, image=imagen).pack(side="left")


#Creamos un nuevo frame para los checkbuttons
frame = Frame(root)
frame.pack(side="right") 

#Creamos Label
Label(frame, text="What kind of coffe Would you like to have ?").pack(anchor="w")
Checkbutton(frame, text="Milk", variable=milk, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Sugar", variable=sugar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

#Obtener nos valores
monitor = Label(frame)
monitor.pack()


#loop
root.mainloop()