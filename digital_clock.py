#a program using tkinter to display time
from tkinter import *
from tkinter.ttk import *
from time import strftime

def update_time():
    current = strftime("%I:%m:%S %p")
    label.config(text=current)
    label.after(1000,update_time)

root=Tk()
root.geometry("530x100")
root.title("a digital clock")
root.iconbitmap("images/icon.ico")
label=Label(root,text="start",font=("Ariel",70),background="black",foreground="cyan")
label.pack()
update_time()
root.mainloop()