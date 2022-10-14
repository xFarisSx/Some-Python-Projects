from tkinter import *


root = Tk()
#creat a label , (and show it)
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="my name is john elder").grid(row=1, column=5)
myLabel3 = Label(root, text="      ").grid(row=1, column=1)

#show it
# myLabel1.grid(row=0, column=0)# relative
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=1, column=1)

root.mainloop()