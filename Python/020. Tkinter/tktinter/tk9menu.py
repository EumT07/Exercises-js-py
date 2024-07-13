from tkinter import *

#Raiz
root = Tk()

#opciones
root.config(bg="black")
root.iconbitmap("images.ico")
root.title("Hengar")
root.resizable(0,0)
root.config(width=250,height=200)

#Menu
menuBar = Menu(root)#Menu Principal
root.config(menu=menuBar)


#Añadiar elementos o submenus
#tearoff = 0, Para eliminar la pequeña seccion que aparece
filemenu = Menu(menuBar, tearoff=0)#File Option
editmenu = Menu(menuBar, tearoff=0)#Edit Option
helpmenu = Menu(menuBar, tearoff=0)#Help Option

#Mostrar los menu -> titulo dentro del menu Principal

#File Option
menuBar.add_cascade(label="File",menu=filemenu)
#Introduciendo opciones:
filemenu.add_command(label="New File")
filemenu.add_command(label="Open File")
filemenu.add_command(label="Save File")
filemenu.add_command(label="Adv Options")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

#Edit Options
menuBar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="cut")
editmenu.add_command(label="Clean")
editmenu.add_separator()
#Another menu inside edit
optionmenu = Menu(editmenu, tearoff=0)

editmenu.add_cascade(label="More Options", menu=optionmenu)
optionmenu.add_command(label="filter")
optionmenu.add_command(label="Sizes")
optionmenu.add_command(label="rename")

#Help Options
menuBar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="How creat..")
helpmenu.add_command(label="Save Problem")
helpmenu.add_separator()
helpmenu.add_command(label="About ...")



#loop
root.mainloop()