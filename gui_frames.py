<<<<<<< HEAD
from tkinter import Tk, Frame, Button, BOTTOM, LEFT, RIGHT, Y
langas = Tk()
langas.geometry("400x300")
# freimai
virsutinis = Frame(langas)
apatinis = Frame(langas)
# mygtukai freimuose
mygtukas1 = Button(virsutinis, text="Pirmas")
mygtukas2 = Button(virsutinis, text="Antras")
mygtukas3 = Button(virsutinis, text="Trečias")
mygtukas4 = Button(apatinis, text="Paskutinis")
=======
from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y
langas = Tk()
langas.geometry("500x300")
# susikuriam freimus
virsutinis = Frame(langas)
apatinis = Frame(langas)
# susikuriam mygtukus
mygtukas1 = Button(virsutinis, text="Pirmas")
mygtukas2 = Button(virsutinis, text="Antras")
mygtukas3 = Button(virsutinis, text="trecias")
mygtukas4 = Button(apatinis, text="paskutinis")
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
# pakuojam
virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
<<<<<<< HEAD
mygtukas4.pack(side=BOTTOM, fill=Y)
# paleidziam
=======
mygtukas4.pack(side=BOTTOM,fill=Y)
#paleidziam
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
langas.mainloop()
