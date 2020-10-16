#https://youtu.be/YXPyB4XeYLA
from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert("Enter Your Name: ")

def myClick():
    myLabel = Label(root, text=f"Hello {e.get()}")
    myLabel.pack()

myButton = Button(root, text="Enter your name", padx=50, pady=50, command=myClick)
myButton.pack()

root.mainloop()
