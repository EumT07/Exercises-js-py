import tkinter


from tkinter import *


#Funcion
def selecionar():
    monitor.config(text=f"{opcion.get()}")

def reset():
    opcion.set(None)
    monitor.config(text="")



#Raiz
root = Tk()

#dato a selecionar
opcion = IntVar()

Radiobutton(root, text="Opcion 1", variable=opcion, value=1, command=selecionar).pack()
Radiobutton(root, text="Opcion 2", variable=opcion, value=2, command=selecionar).pack()
Radiobutton(root, text="Opcion 3", variable=opcion, value=3, command=selecionar).pack()
OptionMenu(root,StringVar(),"hola").pack()


monitor = Label(root)
monitor.pack()

#Boton para reiniciar
Button(root, text="Reiniciar", command=reset, bg="red").pack()



#Bucle
root.mainloop()