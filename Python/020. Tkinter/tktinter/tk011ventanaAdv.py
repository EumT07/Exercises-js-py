from tkinter import *
from tkinter import messagebox as Messagebox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

#Raiz

root = Tk()
root.title("Hengar")
root.config(bg="black", width=200,height=29,bd=20,padx=20,pady=20)
root.resizable(0,0)
root.iconbitmap("images.ico")
#popups
def test():

    # Elegir un color

    color = ColorChooser.askcolor(title="Choose a color")
    print(color)# Obtendra el color
     
     #Elegir un file

     # Ruta / ubicacion
     # Se puede establecer rutas de inicio 
     #Dentro de filetypes crear ((tupla),) - colocar , 
     #Esto es para poder crear como minimo una tupla
     # ("File text","*.txt"),("files adv text","*txt2"),("All files","*.*")

    # ruta = FileDialog.askopenfilename(title="Open new file", initialdir="C:", filetypes=(("File text","*.txt"),("files adv text","*txt2")))
    # print(ruta)

    #Guardar un file
    #Equivale a open("ruta","w")
    #Dentro de la carpeta donde se desea guardar. 
    file = FileDialog.asksaveasfile(title="Saves File", mode="w", defaultextension=".txt")
    if file is not None:
        file.write("Hola amigos")
        file.close()
    # print(file) # va sobresescribir el file
        




button = Button(root, text="Click", command=test)
button.pack()





#loop
root.mainloop()