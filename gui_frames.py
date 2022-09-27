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
# pakuojam
virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM,fill=Y)
#paleidziam
langas.mainloop()
