from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = e_zodis.get()
    l_rezultatas["text"] = ivesta
    e_zodis.delete(0, len(ivesta))

l_zodis = Label(langas, text="Įveskite žodį:")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="pavirtinti", command=spausdinti)
langas.bind("<Return>", lambda event: spausdinti())
l_rezultatas = Label(langas, text="")

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3)

langas.mainloop()
