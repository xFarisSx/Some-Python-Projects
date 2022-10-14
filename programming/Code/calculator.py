from tkinter import *
import tkinter

penc = tkinter.Tk()

penc.geometry("320x300")

penc.title("Simple Calculator")

def topla():
    if sa1.get().isdigit() and sa2.get().isdigit():
        s1 = float(sa1.get())
        s2 = float(sa2.get())
        sonuc.configure(text = str(s1 + s2))

def cikar():
    if sa1.get().isdigit() and sa2.get().isdigit():
        s1 = float(sa1.get())
        s2 = float(sa2.get())
        sonuc.configure(text = str(s1 - s2))

def carp():
    if sa1.get().isdigit() and sa2.get().isdigit():
        s1 = float(sa1.get())
        s2 = float(sa2.get())
        sonuc.configure(text = str(s1 * s2))

def bol():
    if sa1.get().isdigit() and sa2.get().isdigit():
        s1 = float(sa1.get())
        s2 = float(sa2.get())
        sonuc.configure(text = str(s1 / s2))

def us():
    if sa1.get().isdigit() and sa2.get().isdigit():
        s1 = float(sa1.get())
        s2 = float(sa2.get())
        sonuc.configure(text = str(s1 ** s2))


sonuc = Label(penc, text = "sonuc", font = "courier", width= 30, justify="center")
sonuc.place(x = 0, y = 20)


sa1 = Entry(penc, font = "courier" , width= 15, justify="right")
sa1.place(x = 80, y = 50)
sa1.focus()


sa2 = Entry(penc,  font = "courier", width= 15, justify="right")
sa2.place(x = 80, y = 80)


toplama = Button(penc, text= "+", width= 20, command=topla  )
toplama.place(x = 80, y = 110)


cikarma = Button(penc, text= "-", width= 20 , command=cikar )
cikarma.place(x = 80, y = 140)


carpma = Button(penc, text= "x", width= 20  ,command=carp )
carpma.place(x = 80, y = 170)


bolme = Button(penc, text= "/", width= 20, command=bol )
bolme.place(x = 80, y = 200)


usa = Button(penc, text= "^", width= 20, command=us)
usa.place(x = 80, y = 230)


penc.mainloop()