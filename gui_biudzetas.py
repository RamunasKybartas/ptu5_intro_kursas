# from operator import attrgetter
# from datetime import datetime
# class Irasas:
#     def __init__(self, suma):
#         self.suma = suma


# class PajamuIrasas(Irasas):
#     def __init__(self, suma, data_laikas, siuntejas, papildoma_informacija):
#         super().__init__(suma)
#         self.siuntejas = siuntejas
#         self.papildoma_informacija = papildoma_informacija
#         self.data_laikas = datetime.strptime(data_laikas, "%Y-%m-%d %H:%M:%S")
        

# class IslaiduIrasas(Irasas):
#     def __init__(self, suma, data_laikas, atsiskaitymo_budas, isigyta_preke_paslauga):
#         super().__init__(suma)
#         self.atsiskaitymo_budas = atsiskaitymo_budas
#         self.isigyta_preke_paslauga = isigyta_preke_paslauga
#         self.data_laikas = datetime.strptime(data_laikas, "%Y-%m-%d %H:%M:%S")


# class Biudzetas():
#     def __init__(self):
#         self.zurnalas = []

#     def prideti_pajamu_irasa(self, suma, data_laikas, siuntejas, papildoma_informacija):
#         pajamu_irasas = PajamuIrasas(suma, data_laikas, siuntejas, papildoma_informacija)
#         self.zurnalas.append(pajamu_irasas)

#     def prideti_islaidu_irasa(self, suma, data_laikas, atsiskaitymo_budas, isigyta_preke_paslauga ):
#         islaidu_irasas = IslaiduIrasas(suma, data_laikas, atsiskaitymo_budas, isigyta_preke_paslauga)
#         self.zurnalas.append(islaidu_irasas)

#     def gauti_balansa(self):
#         balansas = 0
#         for irasas in self.zurnalas:
#             if isinstance(irasas, PajamuIrasas):
#                 balansas += irasas.suma
#             if isinstance(irasas, IslaiduIrasas):
#                 balansas -= irasas.suma
#         return balansas

#     def gauti_ataskaita(self):
#         pagal_data = sorted(self.zurnalas, key=attrgetter("data_laikas"))
#         for irasas in pagal_data:
#             if isinstance(irasas, PajamuIrasas):
#                 print(f"Pajamos: {irasas.suma} eur {irasas.data_laikas} siuntejas: {irasas.siuntejas} papildoma info: {irasas.papildoma_informacija}")
#             if isinstance(irasas, IslaiduIrasas):
#                 print(f"Islaidos: {irasas.suma} eur {irasas.data_laikas} atsiskaitymo budas: {irasas.atsiskaitymo_budas} preke: {irasas.isigyta_preke_paslauga}")

# biudzetas = Biudzetas()


# while True:
#     pasirinkimas = input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos\n...Pasirinkite: ")
#     if pasirinkimas == "1":
#         suma = int(input("Įveskite pajamų sumą: "))
#         siuntejas = input("Iveskite siunteja: ")
#         papildoma_informacija = input("Iveskite papildoma informacija: ")
#         data_laikas = input("Iveskite pajamu data ir laika formatu YYYY-MM-DD hh:mm:ss: ")
#         biudzetas.prideti_pajamu_irasa(suma, data_laikas, siuntejas, papildoma_informacija)
#     if pasirinkimas == "2":
#         suma = int(input("Įveskite išlaidų sumą: "))
#         if suma > biudzetas.gauti_balansa():
#             print(f"Virsinate turima balansa, jusu saskaitoje: {biudzetas.gauti_balansa()}")
#             continue
#         atsiskaitymo_budas = input("Pridekite atsiskaitymo buda: ")
#         isigyta_preke_paslauga = input("Iveskite isigyta preke ar paslauga: ")
#         data_laikas = input("Iveskite islaidu data ir laika formatu YYYY-MM-DD hh:mm:ss: ") 
#         biudzetas.prideti_islaidu_irasa(suma, data_laikas, atsiskaitymo_budas, isigyta_preke_paslauga)
#     if pasirinkimas == "3":
#         print(f"Balansas: {biudzetas.gauti_balansa()}")
#     if pasirinkimas == "4":
#         print(f"Pajamu/Islaidu isklotine\n{biudzetas.gauti_ataskaita()}")
#     if pasirinkimas == "9":
#         print("Viso gero")
#         break

import pickle
from tkinter import *

langas = Tk()
virsus = Frame(langas)
apacia = Frame(langas)


class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas="", papildoma_info=""):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info

    def __str__(self):
        return f"Pajamų suma: {self.suma}"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas="", isigyta_preke_paslauga=""):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return f"Išlaidų suma: {self.suma}"


class Biudzetas():
    def __init__(self):
        self.zurnalas = self.gauti_biudzeta()

    def ivesti_pajamas(self, suma, siuntejas="", papildoma_informacija=""):
        pajamu_irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamu_irasas)
        self.irasyti_biudzeta(self.zurnalas)

    def ivesti_islaidas(self, suma, atsiskaitymo_budas="", isigyta_preke_paslauga=""):
        islaidu_irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidu_irasas)
        self.irasyti_biudzeta(self.zurnalas)

    def gauti_biudzeto_balansa(self):
        balansas = 0
        for irasas in self.gauti_biudzeta():
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return balansas

    def gauti_biudzeta(self):
        try:
            with open("biudzetas.pkl", "rb") as pickle_in:
                biudzetas = pickle.load(pickle_in)
        except:
            biudzetas = []
        return biudzetas

    def irasyti_biudzeta(self, biudzetas):
        try:
            with open("biudzetas.pkl", "wb") as pickle_out:
                pickle.dump(biudzetas, pickle_out)
        except:
            print("Nepavyko įrašyti failo")


mano_biudzetas = Biudzetas()


def ivesti_irasa(event):
    suma = int(suma_laukas.get())
    if suma < 0:
        irasas = IslaiduIrasas(abs(suma))
    else:
        irasas = PajamuIrasas(abs(suma))
    biudzetas = mano_biudzetas.gauti_biudzeta()
    biudzetas.append(irasas)
    mano_biudzetas.irasyti_biudzeta(biudzetas)
    boksas.delete(0, END)
    boksas.insert(END, *mano_biudzetas.gauti_biudzeta())
    balansas_uzrasas["text"] = str(mano_biudzetas.gauti_biudzeto_balansa())
    suma_laukas.delete(0, 'end')


def isvalyti():
    biudzetas = []
    mano_biudzetas.irasyti_biudzeta(biudzetas)
    boksas.delete(0, END)
    balansas_uzrasas["text"] = ""


langas.geometry("250x200")
uzrasas1 = Label(virsus, text="Įrašykite sumą")
suma_laukas = Entry(virsus)
mygtukas = Button(virsus, text="Įvesti")
mygtukas.bind("<Button-1>", ivesti_irasa)
langas.bind("<Return>", ivesti_irasa)
mygtukas2 = Button(virsus, text="Išvalyti", command=isvalyti)
balansas_uzrasas_labas = Label(virsus, text="Balansas:")
balansas_uzrasas = Label(virsus, text=str(mano_biudzetas.gauti_biudzeto_balansa()))

scrollbaras = Scrollbar(apacia)
boksas = Listbox(apacia, yscrollcommand=scrollbaras.set)
scrollbaras.config(command=boksas.yview)
boksas.insert(END, *mano_biudzetas.gauti_biudzeta())

virsus.pack()
apacia.pack()
uzrasas1.grid(row=0, column=0)
suma_laukas.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
scrollbaras.pack(side=RIGHT, fill=Y)
boksas.pack(side=LEFT)
mygtukas2.grid(row=2, column=2)
balansas_uzrasas_labas.grid(row=1, column=1)
balansas_uzrasas.grid(row=1, column=2)
langas.mainloop()