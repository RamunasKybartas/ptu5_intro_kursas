from tkinter import *

langas = Tk()

def spausdinti_su_enter():
    print("spausdina paspaudus ENTER...")

def spausdinti_su_kairiu(event):
    print("spausdina paspaudus kairi")

def spausdinti_su_desiniu(event):
    print("spausdina paspaudus desini")


mygtukas = Button(langas, text="spausdinti")  # command=spausdinti
# bind priskiria funkcija klavisui
mygtukas.bind("<Button-1>", spausdinti_su_kairiu)  # 1- kairys peles
mygtukas.bind("<Button-3>", spausdinti_su_desiniu) # 3- desinys peles, 2- peles scrollas
langas.bind("<Return>", lambda event: spausdinti_su_enter()) # nereikia irasyti event  kintamojo i funkcija
mygtukas.pack()
langas.mainloop()

