from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('radio')

#r = IntVar()
#r.set("2")

modes = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", 'Cheese'),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text,mode in modes:
    Radiobutton(root, text=text,variable=pizza,value=mode).pack(anchor=W)

def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()



# Radiobutton(root,text='1', variable=r,value=1, command=lambda: click(r.get())).pack()
# Radiobutton(root,text='2', variable=r,value=2, command=lambda: click(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

b = Button(root, text='clicked', command=lambda: click(pizza.get()))
b.pack()




root.mainloop()