from tkinter import Tk, Label
# sukuriam lango objekta pagal Tk() klase
langas = Tk()
# nustatom lango dydi
langas.geometry("500x300")
# i langa sukuriam objekta pagal Label() klase
uzrasas = Label(langas, text="Sveiki, visi!")
uzrasas2 = Label(langas, text="Antradieniux")
# supakuojam uzrasa
uzrasas.pack()
uzrasas2.pack(side="bottom")
# paleidziam lango programa
langas.mainloop()
