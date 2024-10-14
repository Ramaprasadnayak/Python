from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def new_file():
    global file
    root.title("untitled-page")
    file=None
    textarea.delete(1.0,END)

def open_file():
    global file
    file=askopenfilename(defaultextension=".txt")

    if file == "":
        file=None
    else:
        try:
            root.title(os.path.basename(file)+"- Notepad")
            textarea.delete(1.0,END)
            f=open(file,"r")
            textarea.insert(1.0,f.read())
            f.close()
        except Exception as e:
            messagebox.showerror("warning","file not found"+str(e))

        
def save():
    global file 
    if file == None:
        file = asksaveasfilename(initialfile='untitled .txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])

        if file == "":
            file=None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()



def exitapp():
    res=messagebox.askyesno("waring!!","you sure you wanna exit")
    if res:
        root.destroy()
    else:
        pass
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    messagebox.showinfo("about","Notepad by Ramprasad-Nayak")
def contactus():
    messagebox.showinfo("contact","for more help contact in email ramprasadnayak999@gmail.com")


root=Tk()
root.title("untitled-page")
root.wm_iconbitmap("icon1.ico")
root.geometry("400x400")


textarea=Text(root,font="lucida 13")
file= None
textarea.pack(expand=True,fill=BOTH)

sc=Scrollbar(textarea)
sc.pack(fill=Y,side=RIGHT)
sc.config(command=textarea.yview)
textarea.config(yscrollcommand=sc.set)


mainmenu=Menu(root)

filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label="new",command=new_file)
filemenu.add_command(label="open",command=open_file)
filemenu.add_separator()
filemenu.add_command(label="save",command=save)
filemenu.add_command(label="exit",command=exitapp)
mainmenu.add_cascade(label="files",menu=filemenu)

editmenu=Menu(mainmenu,tearoff=0)
editmenu.add_command(label="copy",command=copy)
editmenu.add_command(label="paste",command=paste)
filemenu.add_separator()
editmenu.add_command(label="cut",command=cut)
mainmenu.add_cascade(label="edit",menu=editmenu)
root.config(menu=mainmenu)

helpmenu=Menu(mainmenu,tearoff=0)
helpmenu.add_command(label="about",command=about)
helpmenu.add_command(label="contact us",command=contactus)
mainmenu.add_cascade(label="help",menu=helpmenu)

root.mainloop()