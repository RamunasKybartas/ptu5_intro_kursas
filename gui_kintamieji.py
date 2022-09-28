from tkinter import *

langas = Tk()

tekstas = StringVar()

def tekstas_save():
    tekstas.set(entry_tekstas.get())
    entry_tekstas.delete(0, len(entry_tekstas.get()))

def tekstas_load():
    label_tekstas["text"] = tekstas.get()


def tekstas_clear():
    tekstas.set("")
    label_tekstas["text"] = ""
    entry_tekstas.delete(0, len(entry_tekstas.get()))

entry_tekstas = Entry(langas)
label_tekstas = Label(langas, text="")
mygtukas_save = Button(langas, text="save", command=tekstas_save)
mygtukas_load = Button(langas, text="load", command=tekstas_load)
mygtukas_clear = Button(langas, text="clear", command=tekstas_clear)
langas.bind("<Return>", lambda event: tekstas_save())

entry_tekstas.pack()
label_tekstas.pack(side=BOTTOM)
mygtukas_save.pack(side=LEFT)
mygtukas_load.pack(side=LEFT)
mygtukas_clear.pack(side=LEFT)

langas.mainloop()
