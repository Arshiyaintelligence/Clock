
from time import strftime
from tkinter import *
from tkinter.ttk import *

from matplotlib.pyplot import text


root  = Tk()
root.title("Clock !")


label = Label(root , font=("DS-DIGIT",80)  , background="black" , foreground="cyan" )
label.pack(anchor="center")

def time():
    string = strftime('%H:%M:%S  %p')
    label.config(text = string)
    label.after(1000,time)


time()

mainloop()


