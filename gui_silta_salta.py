# from random import randint
# teisingas = randint(-2**15, 2**15) 
# spejimas = None
# skirtumas = 0
# kartai = 0
# while spejimas is None or spejimas != teisingas:
#     try:
#         spejimas = int(input("Spėkite skaičių: "))
#     except ValueError:
#         print("įvestas ne skaičius")
#     else:
#         kartai += 1
#         if teisingas != spejimas:
#             if abs(teisingas - spejimas) < skirtumas:
#                 print(spejimas, "šilta...")
#             else:
#                 print(spejimas, "šalta...")
#             skirtumas = abs(teisingas - spejimas)
# else:
#     print(f"!!! Atspėjai iš {kartai} karto. Teisingas atsakymas: {teisingas}")

from tkinter import *
from random import randint

langas = Tk()
teisingas = randint(-100, 100)
kartai = IntVar()
skirtumas = IntVar()

def spejimas():
    try:
        skaicius = int(entry_spejimas.get())
    except ValueError:
        atsakymas["text"] = "Įvestas ne skaičius"
    else:
        kartai.set(kartai.get()+1)
        if skaicius != teisingas:
            if abs(teisingas - skaicius) < skirtumas.get():
                atsakymas["text"] = f"{skaicius}, šilta... "
            else:
                atsakymas["text"] = f"{skaicius}, šalta... "
        skirtumas.set(abs(teisingas - skaicius)) 
        if skaicius == teisingas:
            atsakymas["text"] = f"atspeta! {skaicius} iš {kartai.get()} karto "
    entry_spejimas.delete(0, len(entry_spejimas.get()))
        
spejimas_tekstas = Label(langas, text="Spėkite skaičių: ")
entry_spejimas = Entry(langas)
mygtukas = Button(langas, text="spėti", command=spejimas)
atsakymas = Label(langas, text="laukiama spėjimo...", bd=2, relief=SUNKEN)
entry_spejimas.bind("<Return>", lambda event: spejimas())

spejimas_tekstas.grid(row=0, column=0)
entry_spejimas.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
atsakymas.grid(row=1, columnspan=3, sticky=W+E)

langas.mainloop()



