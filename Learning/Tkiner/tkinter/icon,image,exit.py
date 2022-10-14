from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("icon")
#root.iconbitmap(location)

my_img = ImageTk.PhotoImage(Image.open('indir.jfif'))
my_Label = Label(image=my_img)
my_Label.pack()


















button_quit=Button(root,text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()