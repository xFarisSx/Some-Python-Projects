from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue",fg="white",borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    hello = f"Hello {e.get()}"
    myLabel = Label(root,text=hello)
    myLabel.pack()


myButton = Button(root, text="enter your name", padx=25, command=myClick, fg="red",bg="blue")

myButton.pack()

root.mainloop()