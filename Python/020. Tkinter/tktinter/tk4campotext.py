from cProfile import label
from tkinter import *
root = Tk()
root.title("Hengar")
root.iconbitmap("images.ico")
root.config(width=250,height=100)


"""
Entry: sirve para insertar texto, ejemplo para recibir informacion y crear un usuario.
"""

#=========== Frame ==========#

# #Frame 1 --> para organizar los widgets
# frame1 = Frame(root)
# frame1.pack()

# label1 = Label(frame1, text="Nombre")
# label1.pack(side="left")#Posicion 

# entry1 = Entry(frame1)
# entry1.pack(side="right")

# # #Frame 2 --> para organizar los widgets
# frame2 = Frame(root)
# frame2.pack()

# label2 = Label(frame2, text="Contraseña")
# label2.pack(side="left")

# entry2 = Entry(frame2)
# entry2.pack(side="right")

#=========== Grid ==========#
#Posicionar los elementos de una mejor forma

#Grid 1
label1 = Label(root, text="Nombre")
label1.grid(row=0,column=0, sticky="w", padx=8,pady=8)
#Sticky: alinear los textos
#padx - pday Padding

entry1 = Entry(root)
entry1.grid(row=0,column=1,padx=8,pady=8)
entry1.config(justify="center", state="disable")
#state = disable -> para desactivar el campo

# Grid 2
label2 = Label(root, text="Pass")
label2.grid(row=1,column=0, sticky="w",padx=8,pady=8)

entry2 = Entry(root)
entry2.grid(row=1,column=1,padx=8,pady=8)
#Password
entry2.config(justify="left", show="*")


root.mainloop()