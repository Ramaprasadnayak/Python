#my first tkinter project
from tkinter import *
from tkinter import messagebox
import math
memo=0

def one():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'1')
    else:
        e1.insert(END,'1')
def two():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'2')
    else:
        e1.insert(END,'2')
def three():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'3')
    else:
        e1.insert(END,'3')
def four():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'4')
    else:
        e1.insert(END,'4')
def five():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'5')
    else:
        e1.insert(END,'5')
def six():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'6')
    else:
        e1.insert(END,'6')
def seven():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'7')
    else:
        e1.insert(END,'7')
def eight():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'8')
    else:
        e1.insert(END,'8')
def nine():
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'9')
    else:
        e1.insert(END,'9')
def zero():
    if e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'0')
    else:
        e1.insert(END,'0')
def plus():
    if e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'+')
    else:
        e1.insert(END,'+')
def minus():
    if e1.get()=='Error' or e1.get()=='0':
        e1.delete(0,END)
        e1.insert(END,'-')
    else:
        e1.insert(END,'-')
def multiply():
    if e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'*')
    else:
        e1.insert(END,'*')
def percent():
    if e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'%')
    else:
        e1.insert(END,'%')
def division():
    if e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'/')
    else:
        e1.insert(END,'/')
def clear():
    e1.delete(0,END)
    e1.insert(END,'0')
def dot():
    if e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,'.')
    else:
        e1.insert(END,'.')

def dele():
    if e1.get()=='0':
        pass
    else:
        d=len(e1.get())-1
        e1.delete(d,END)


def equal():
    try:
        ans=eval(e1.get())
        e1.delete(0,END)
        e1.insert(END,ans)
    except Exception as e:
        e1.delete(0,END)
        e1.insert(END,"Error")
        messagebox.showerror("Error",f"Error in {e}")

def memoplus():
    try:
        global memo
        memo+=float(e1.get())
    except Exception as e:
        e1.delete(0,END)
        e1.insert(END,"Error")
        messagebox.showerror("Error",f"Error in {e}")

def memominus():
    try:
        global memo
        memo-=float(e1.get())
    except Exception as e:
        e1.delete(0,END)
        e1.insert(END,"Error")
        messagebox.showerror("Error",f"Error in {e}")
def memodisp():
    global memo
    if e1.get()=='0' or e1.get()=='Error':
        e1.delete(0,END)
        e1.insert(END,memo)
    else:
        e1.insert(END,memo)
    
def square():
    try:
        value=int(e1.get())
        ans=math.pow(value,2)
        e1.delete(0,END)
        e1.insert(END,ans)
    except Exception as e:
        e1.delete(0,END)
        e1.insert(END,"Error")
        messagebox.showerror("Error",f"Error in {e}")

def squareroot():
    try:
        ans=math.sqrt(int(e1.get()))
        e1.delete(0,END)
        e1.insert(END,ans)
    except Exception as e:
        e1.delete(0,END)
        e1.insert(END,"Error")
        messagebox.showerror("Error",f"Error in {e}")

def log():
    try:
        ans=math.log10(int(e1.get()))
        e1.delete(0,END)
        e1.insert(END,ans)
    except Exception as e:
        e1.delete(0,END)
        e1.insert(END,"Error")
        messagebox.showerror("Error",f"Error in {e}")


root=Tk()
root.title("calculator")
root.geometry("350x345")
root.minsize(350,345)
root.maxsize(350,345)
f1=Frame(root,bg="black",bd=30,relief="raised")
f1.pack(fill=BOTH,expand=True)
f2=Frame(f1,bg="grey",relief="sunken",bd=10)
f2.pack(padx=10,pady=10)

e1=Entry(f2,font="lucida 13")
e1.pack(padx=10,pady=10)
e1.insert(END,0)

button=[("M+",memoplus),("M-",memominus),("M",memodisp),("sqr",square),("sqrt",squareroot),
        ("7",seven),("8",eight),("9",nine),("log",log),("del",dele),
        ("4",four),("5",five),("6",six),("+",plus),("-",minus),
        ("1",one),("2",two),("3",three),("x",multiply),("/",division),
        ("AC",clear),("0",zero),(".",dot),("=",equal),("%",percent)]
xas=18
yas=80
back="blue"
fore="white"
for (number,text) in button:
    Button(f1,text=number,command=text,bg=back,fg=fore).place(x=xas,y=yas,height=40,width=50)
    xas=xas+50
    if xas > 130:
        back="grey"
        fore="black"
    if xas > 230:
        back="grey"
        fore="black"
        yas+=40
        xas=18
    

root.mainloop()
