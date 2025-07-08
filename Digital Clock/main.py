import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

lable = tk.Label(root, background="black", font=("calibri", 50, 'bold'), foreground="white")
lable.pack(anchor='center')

def time():
    string = strftime('%H:%M:%S %p \n %D')
    lable.config(text=string)
    lable.after(1000, time)

time()
root.mainloop()

