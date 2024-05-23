from tkinter import *

root = Tk()

root.title("Крутое приложение")
root.geometry("400x400")
root.resizable(True, True) #x y
root.minsize(300, 300)
# root.maxsize(500, 500)

# root.iconbitmap(default="flaticon.png")
icon = PhotoImage(file = "flaticon.png")
root.iconphoto(True, icon)

hello_label = Label(text="Hello my friends!")
hello_label.pack()

def finish():
    root.destroy()
    print('окно закрыто')

root.protocol("WM_DELETE_WINDOW", finish)

root.attributes("-alpha", 1)
root.attributes("-fullscreen", False)

root.mainloop()



