from tkinter import *
from tkinter.filedialog import askopenfilename ,asksaveasfilename
import tkinter.messagebox as tmsg
import os

root=Tk()
root.geometry("400x410")
root.title("Untitled- Notepad")

# for Scrollbar
# 1.   widget(yscrollcommand=scrollbar.set)
# 2.   scrollbar.config(command=widget.yview)

def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    text.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filestype=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
            file
        

def cut():
    text.event_generate(("<<Cut>>"))
    
def copy():
    text.event_generate(("<<Copy>>"))
    
def paste():
    text.event_generate(("<<Paste>>"))
    
def about():
    tmsg.showinfo("About us","Please Contact Abhinav for any Help.")

scrollbar=Scrollbar(root)
scrollbar.pack(side="right",fill="y")

text=Text(root,height=100,yscrollcommand=scrollbar.set)          # Takes Text Input
file=None
text.pack(fill="both")

scrollbar.config(command=text.yview)

yourmenu=Menu(root)                                   # Menu Bar

m1=Menu(yourmenu,tearoff=0)                      # tearoff=0 is used to stop taking out the full menubar
m1.add_command(label="New File",command=newfile)
m1.add_command(label="Open",command=openfile)                              # Submenu
m1.add_command(label="Save",command=savefile)
m1.add_separator()
m1.add_command(label="Exit",command=root.destroy)
root.config(menu=yourmenu)

yourmenu.add_cascade(label="File",menu=m1)                  # Menu

m2=Menu(yourmenu,tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
root.config(menu=yourmenu)

yourmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(yourmenu,tearoff=0)
m3.add_command(label="About",command=about)
root.config(menu=yourmenu)

yourmenu.add_cascade(label="Help",menu=m3)

root.mainloop()
