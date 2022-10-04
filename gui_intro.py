from tkinter import Tk, Label
<<<<<<< HEAD

# sukuriam lango objekta pagal Tk() klasę
langas = Tk()
# nustatom lango dydį
langas.geometry("500x300")
# į langą sukuriam `uzrasas` objektą pagal Label klasę, su tekstu
uzrasas = Label(langas, text="Sveiki, studentai!")
uzrasas2 = Label(langas, text="Smagus antradienis")
# supkauojam uzrasas
uzrasas.pack()
uzrasas2.pack(side='bottom')
# paleidžiam lango programą
=======
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
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
langas.mainloop()
