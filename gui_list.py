from tkinter import *

langas = Tk()

def spausdinti():
<<<<<<< HEAD
    try:
        pasirinkta = sarasas[dezute.curselection()[0]]
    except IndexError:
        label_pasirinkta["text"] = "NIEKO!"
    else:
        label_pasirinkta["text"] = pasirinkta

dezute_scroll = Scrollbar(langas)
# listbox'ui priskiriam scrollbar'ą, listbox'o plotis 5, pasirinkti galima tik po vieną
dezute = Listbox(langas, yscrollcommand=dezute_scroll.set, width=5, selectmode=SINGLE)
# scrollbaro pizicija atsinaujins, prastūmus listbox'ą kitais būdais (ne su scrollbaru)
dezute_scroll.config(command=dezute.yview)
sarasas = range(1983, 2023)
dezute.insert(END, *sarasas)
label_pasirinkta = Label(langas, text="Pasirinkite!")
button_pasirinkti = Button(langas, text="Rinktis", command=spausdinti)
# pack and go
dezute.pack(side=LEFT, fill=Y)
dezute_scroll.pack(side=RIGHT, fill=Y)
button_pasirinkti.pack()
label_pasirinkta.pack()
=======
    # if dezute.curselection()[0]>-1:
    try:
        pasirinkta = sarasas[dezute.curselection()[0]]   #sarase yra tikri duomenys, dezute yra ju reprezentacija
    except IndexError:
        label_pasirinkta["text"] = "Nieko\n nepasirinkote!"
    else:
        label_pasirinkta["text"] = pasirinkta





dezute_scroll = Scrollbar(langas)
# listboxui priskiriam scrollbara, kurio plotis=15, pasirinkti is jo galima viena elementa
dezute = Listbox(langas, yscrollcommand=dezute_scroll.set, width=15, selectmode=SINGLE)
# scrollbaro pozicija atsinaujins, prastumus listboxa kitais budais (ne su scrollbar)
dezute_scroll.config(command=dezute.yview)
sarasas = range(1990, 2023)
dezute.insert(END, *sarasas) # deda nuo galo saraso, jeigu 0 nuo pradzios
# dezute.insert(0, *sarasas[:10])
# dezute.insert(0, *sarasas[10:])
label_pasirinkta = Label(langas, text="Pasirinkite!")
button_pasirinkti = Button(langas, text="Rinktis", command=spausdinti)
# pack and go
dezute_scroll.pack(side=RIGHT, fill=Y)
dezute.pack(side=LEFT, fill=Y)
button_pasirinkti.pack()
label_pasirinkta.pack()

>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
langas.mainloop()
