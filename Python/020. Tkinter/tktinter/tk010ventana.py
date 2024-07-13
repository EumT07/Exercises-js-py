from tkinter import *
from tkinter import messagebox as Messagebox

#Raiz

root = Tk()
root.title("Hengar")
root.config(bg="black", width=200,height=29,bd=20,padx=20,pady=20)
root.resizable(0,0)
root.iconbitmap("images.ico")
#popups
def test():

    # Alert Windows show info

    # Messagebox.showinfo("Eyy","Welcome")
    # Messagebox.showwarning("Alert", "You need to adm Permission")
    # Messagebox.showerror("Err..!!","There is an Error, please check it out")

    #Alert ask user something:

    #Question --> ask something : askquestion
    result = Messagebox.askquestion("Exit","Are you sure you want to 'Exit' ?")
    #answer
    if(result == "yes"): # "yes" : # "no"
        root.destroy()


    # #Question --> realizar acciones : askokcancel 
    # result = Messagebox.askokcancel("Exit","Do you want rename the file?")
    # #answer
    # if result == True:
    #     root.destroy()

    # # Question --> realizar acciones : askyesno
    # result = Messagebox.askyesno("Exit","Do you exit without save the file?")
    # #answer
    # if result == True:
    #     root.destroy()


    # # Question --> realizar acciones : asktrycancel
    # result = Messagebox.askretrycancel("Retry","Do you retray again?")
    # #answer
    # if result == True:
    #     root.destroy()


button = Button(root, text="Click", command=test)
button.pack()





#loop
root.mainloop()





