from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = e_zodis.get()
    l_rezultatas["text"] = ivesta
    e_zodis.delete(0, len(ivesta))

<<<<<<< HEAD
l_zodis = Label(langas, text="Įveskite žodį:")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="pavirtinti", command=spausdinti)
=======


l_zodis = Label(langas, text="Iveskite zodi: ")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
langas.bind("<Return>", lambda event: spausdinti())
l_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, anchor=W)

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
<<<<<<< HEAD
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=W+E)

langas.mainloop()
=======
mygtukas.grid(row=0,column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=W+E)

langas.mainloop()
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
