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



#Asiganar valores/configurar/editar a la ventana
root.config(cursor="arrow")
root.config(width=150, height=200)
# root.config(bg="black")
root.config(bd=14)
root.config(relief="flat")

#============ Frames =============#
#Se le pasa la raiz, donde se va trabajar. 
#width: Tamaño  horizontal (Ancho)
#height: tamaño vertical (Alto)
frame1 = Frame(root, width=450, height=500)

#Pack -> que se distribuya dentro de root
frame1.pack()

frame1.pack(side="left")#Posicion del frame
#frame1.pack(side="left", anchor="W")#Posicion del frame
# frame1.pack(fill="x", expand=1)

"""
fill x Ancho horizontal
fill y ancho vertical  
Expand se rellenara en vertial: siempre y cuando no tengas 
un tamañano por defecto en el root
anchor --> orientacion, north south east west
"""

#config --> para configurar la ventana
frame1.config(cursor="pirate")

frame1.config(bg="black")
frame1.config(bd=25)
frame1.config(relief="groove")

root.mainloop()