from cgitb import text
from posixpath import normpath
from tkinter import *
root = Tk()


#Assignar name
root.title("Hengar")
#Ajustar medidas (altur,anchura)
root.resizable(1,1)
#Asiganar una imagen-ico
root.iconbitmap("images.ico")



#Asiganar valores a la ventana
root.config(cursor="arrow")
root.config(width=150, height=200)
# root.config(bg="black")
root.config(bd=14)
root.config(relief="flat")


#============ Label =============#
#Cambiar el texto dinamicamente
#variables
texto = StringVar()
texto.set("Oyeee")

#Normal con el pack
label = Label(root, text="Hola Bienvenido a Hengar")
label.pack()
label.place(x=0, y=50)
# Varios Labels
# Horientacion con side:
# Label(root, text="Hola Bienvenido a Hengar").pack(side="left")
# Label(root, text="Que deseas hacer").pack()
# Label(root, text="Tu decides").pack(side="right")

#Horientacion con anchor:
Label(root, text="Hola Bienvenido a Hengar").pack(anchor="nw")
label = Label(root, text="Que deseas hacer")
label.pack(anchor="center")
Label(root, text="Tu decides").pack(anchor="se")
label.config(bg="red", fg="yellow", font=("Verdana",16))
label.config(textvariable=texto)

# imagen = PhotoImage(file="hengar.gif")
# Label(root, image=imagen, bd=0).pack(anchor="center")
#Debe ir al final
root.mainloop()