import sqlite3
from tkinter import *

root = Tk()
root.title(" --Bar Menu--  ")
root.resizable()

#Crear 

Label(root, text=" Bar El Margariteño ", fg="darkblue", font=("Times nnew Roman",16,"bold italic")).pack()

Label(root, text="Menú del dia",fg="green",font=("Times New Roman",10,"bold italic")).pack()

#break#
Label(root, text="").pack

#data base Connection

conexion = sqlite3.connect("restaurant.db")
cursor = conexion.cursor()

#Buscar categorias:

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=categoria[1], fg="black", font=("Times New Roman", 20, "bold")).pack()

    platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id={categoria[0]}").fetchall()      
    for plato in platos:
            Label(root, text=plato[1], fg="gray",font=("Verdana",14,"italic")).pack()

    #break#
    Label(root, text="").pack


Label(root, text="$ 12(IVA incl", fg="blue", font=("Times New Roman", 20, "bold")).pack()

root.mainloop()

