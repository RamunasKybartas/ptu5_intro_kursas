# 1 užduotis
# Sukurti programą su grafine sąsaja, kuri:

# Turėtų laukelį su užrašu "Įveskite vardą", 
# kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", 
# kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"

from tkinter import *




langas = Tk()

# langas.geometry("300x500")
meniukas = Menu(langas)
langas.config(menu=meniukas)
submeniukas = Menu(meniukas, tearoff=0)
sarasas = []

def spausdint():
    ivesta = vardo_entry.get()
    isvestis["text"] = f"Labas, {ivesta}"
    vardo_entry.delete(0, len(ivesta))
    sarasas.append(isvestis["text"])
    status_baras["text"] = "Sukurta"
    
def teksto_istrynimas():
    isvestis["text"] = ""
    status_baras["text"] = "Isvalyta"

def teksto_atkurimas():
    isvestis["text"] = sarasas[-2]
    status_baras["text"] = "Atkurta"

def uzdaryti():
    langas.destroy()



iveskite_varda = Label(langas, text="Iveskite varda")
vardo_entry = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdint)
vardo_entry.bind("<Return>", lambda event: spausdint())
isvestis = Label(langas, text="")
status_baras = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)
langas.bind("<Escape>", lambda event: uzdaryti())


meniukas.add_cascade(label="Meniu", menu=submeniukas)
submeniukas.add_command(label="Isvalyti", command=teksto_istrynimas)
submeniukas.add_command(label="Atkurti paskutini", command=teksto_atkurimas)
submeniukas.add_separator()
submeniukas.add_command(label="Iseiti", command=quit)

iveskite_varda.grid(row=0, column=0)
vardo_entry.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
isvestis.grid(row=1, columnspan=3)
status_baras.grid(row=2, columnspan=3, sticky=W+E)


langas.mainloop()

