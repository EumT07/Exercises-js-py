from tkinter import *


#Funcion
# def hola():
#     print("Hola")

# def label_print():
#     Label(root,text="Imprido despues de click").pack()


#Funciones matematicas
def sumar():
    r.set( float(n1.get()) + float(n2.get()))
    borrar()
def resta():
    r.set( float(n1.get()) - float(n2.get()))
    borrar()
def multiplicar():
    r.set( float(n1.get()) * float(n2.get()))
    borrar()

#Borrar campos
def borrar():
    n1.set("")
    n2.set("")

#raiz
root = Tk()
root.title("HENGAR")
root.iconbitmap("../images.ico")
root.config(bd=20)

n1 = StringVar()
n2 = StringVar()
r = StringVar()


#Campos de textos

# Primer numero
Label(root, text="Numero 1").pack()
Entry(root,justify="center",textvariable=n1).pack()
# Segundo numero
Label(root, text="Numero 1").pack()
Entry(root,justify="center",textvariable=n2).pack()

Label(root, text="Resultado").pack()
Label(root,text="").pack()
Entry(root,justify="center",textvariable=r, state="disable").pack()# R
Label(root,text="").pack()

#Buttons

# Button(root,text="Click", command=label_print).pack()
Button(root,text="Sumar", command=sumar).pack(side="left", padx=5)
Button(root,text="Restar", command=resta).pack(side="left",padx=5)
Button(root,text="Multiplicar", command=multiplicar).pack(side="left",padx=5)


#rBucle
root.mainloop()
