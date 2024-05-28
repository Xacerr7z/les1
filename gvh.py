# def bool(x):
#    if x:
#        return 'yes'
#    else:
#        return 'No'

#bool('3 > 2')
    
from tkinter import *
from tkinter import ttk

click = 1

def clicky():
    global click
    click = click * 2

    btn["text"] = f"Cyc {click}"

root = Tk()
root.title("Buttion")
root.geometry('450x450')
btn = ttk.Button(text="Click Me", command=clicky)
btn.pack()

root.mainloop()