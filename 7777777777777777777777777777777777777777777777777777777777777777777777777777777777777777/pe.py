import tkinter as tk
import random

def ciimc():
    min_namber = 1
    max_namber = 100
    secret_number = random.randint(min_namber, max_namber)

    def check_guess():
        print(1)
# try:
#except ValueError:
#none

    window = tk.Tk()
    window.title('игра угодай число')

    welcome_label = tk.Label(window, text=f"я загадал число от {min_namber} до {max_namber}, \n попробуй его угодать!", font=("Helvetica", 50), pady=15, padx=30)
    welcome_label.pack()

    entery = tk.Entry(window)
    entery.pack()

    guess_button = tk.Button(window, text="проверить", command=check_guess,  font=("Helvetica", 14), pady=8, padx=80, background='#FF0000')
    guess_button.pack(pady=15)

    window.mainloop()

if __name__ == "__main__":
    ciimc()








