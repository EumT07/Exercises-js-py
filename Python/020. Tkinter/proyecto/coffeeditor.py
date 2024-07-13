from email import message
from tkinter import *
from tkinter import filedialog as Filedialog
from tkinter import colorchooser as Colorchooser
from tkinter import messagebox as Messagebox

# from os import open

#Global variable, we used this to get file location
route = ""

#Function File edit
def new_file():
    #Referent to external route
    global route
    message.set("New File")
    route = ""
    #Delete content and open new file
    #Star deleting from the first line to end, but it still keep its line break.
    text.delete(1.0,"end")

def open_file():
    global route
    message.set("Open File")
    route = Filedialog.askopenfilename(
        initialdir="./",
        filetypes=(("File text","*.txt"),),
        title="Open new file")
    root.title("Coofeeditor")

    if route != "":
        file = open(route, "r")
        content = file.read()
        #Delete text inside textEditor
        text.delete(1.0,"end")
        text.insert("insert",content)
        file.close()
        root.title(route + "- Coofeeditor")

def save_file():
    message.set("Save File")
    #"end-1c" -> delete the last Character in order to delete line break at the end of text
    if route != "":
        content = text.get(1.0,"end-1c")
        file = open(route,"w+")
        file.write(content)
        file.close()
        message.set("File was saved correctly")
    else:
        saveas_file()
    
def saveas_file():
    global route
    message.set("Save File as")
    file = Filedialog.asksaveasfile(title="Save file", mode="w",defaultextension=".txt")
    if file is not None:
        route = file.name
        content = text.get(1.0,"end-1c")
        file = open(route,"w+")
        file.write(content)
        file.close()
        message.set("File was saved correctly")
    else:
        message.set("It was canceled")
        route = ""

def exitComma():
    global route
    content = text.get(1.0,"end-1c")
    if len(content) == 0:
        root.quit()
    else:
        result = Messagebox.askquestion("Exit","Are you sure you want to Exit without save?")
        if(result == "yes"):
            root.quit()
        else:
            save_file()

#Function Colors

def backgroundColor():
    bgColor = Colorchooser.askcolor(title="Choose a color")    
    text.config(bg=bgColor[1])
def fontletterColor():
    fontColor = Colorchooser.askcolor(title="Choose a color")
    text.config(fg=fontColor[1])

#Root
root = Tk()
# root.overrideredirect(True)#Elimina los botones

#root setting
root.title("Coofeeditor")
root.iconbitmap("coffee.ico")

# Create Menu
menuBar = Menu(root)

# Menu Content
#File
filemenu = Menu(
    menuBar,
    background="#ff8000", 
    foreground="black",
    activebackground="blue", 
    activeforeground="white", 
    tearoff=0)
#Settings
setting = Menu(
    menuBar,
    background="#ff8000", 
    foreground="black",
    activebackground="blue", 
    activeforeground="white", 
    tearoff=0)

#File menu options
filemenu.add_command(label="New File", command=new_file)
filemenu.add_command(label="Open File", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as", command=saveas_file)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=exitComma)
# File Menu content name
menuBar.add_cascade(label="File",menu=filemenu)

#Text complement
text = Text(root)
text.pack(fill="both",expand=1)
#border, background color
# defineText_backGround()
text.config(bd=0, bg="black",padx=6,pady=4)
#font, FontColor
text.config(font=("Consolas",12), fg="white")
#Monitor 
# 1 variables
message = StringVar()
# 2 Set message will show
message.set("Welcome to the best Editor")
# 3 creat a monitor
monitor = Label(root, textvariable=message, justify="left")
monitor.pack(side="left")

#Settings options
setting.add_cascade(label="BackGround Color",command=backgroundColor)
setting.add_cascade(label="Font Color",command=fontletterColor)

#setting menu content name
menuBar.add_cascade(label="Setting",menu=setting)

#root memnu
root.config(menu=menuBar)
#root loop
root.mainloop()