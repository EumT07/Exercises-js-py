from tkinter import *
#Raiz
root = Tk()

#Assignar name
root.title("Hengar")
#Ajustar medidas (altur,anchura)
root.resizable(1,1)
#Ajustar al medio de la ventana
root.eval("tk::PlaceWindow . center")
#Asiganar una imagen-ico
root.iconbitmap("images.ico")



#Asiganar valores a la ventana
root.config(cursor="arrow")
root.config(width=150, height=200)
# root.config(bg="black")
root.config(bd=14)
root.config(relief="flat")



#Debe ir al final, comienza la aplicacion 
root.mainloop()