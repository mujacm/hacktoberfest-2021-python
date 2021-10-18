import random

def generatenumber():
    list=["0","1","2","3","4","5","6","7","8","9","0"]
    number=""
    for i in range(10):
        number=number+random.choice(list)
        l2.config(text=number)
        
import tkinter as tk
window=tk.Tk()
window.geometry("600x200")
window.config(bg="#F39C12")
window.resizable(width=False,height=False)
window.title("Random Number Generator")

l1=tk.Label(text="Random Number Generator",font=("Arial",20),bg="black",fg="white")
b1=tk.Button(text="Generate A Number",font=("Arial",15),bg="#A3E4D7",command=generatenumber)
l2=tk.Label(bg="#F39C12",font=("Arial",30),text="")

l1.place(x=100,y=20)
b1.place(x=165,y=75)
l2.place(x=165,y=130)
window.mainloop()
