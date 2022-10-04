from tkinter import *
import webbrowser

langas = Tk()
langas.geometry("300x100")

meniukas = Menu(langas)
langas.config(menu=meniukas)
submeniukas = Menu(meniukas, tearoff=0)
<<<<<<< HEAD
submeniukas2 = Menu(meniukas, tearoff=0)
=======
submeniukas2 = Menu(meniukas,tearoff=0)
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
submeniukas3 = Menu(meniukas, tearoff=0)

def pirmas():
    label_pasirinkta["text"] = "Pirmas!"

def antras():
    label_pasirinkta["text"] = "Antras!"

def trecias():
<<<<<<< HEAD
    label_pasirinkta["text"] = "Paskutinis iš trijų"

def tell_a_joke():
    label_pasirinkta["text"] = "You are not funny! Haha"

def fart():
    label_pasirinkta["text"] = "pirst.."
=======
    label_pasirinkta["text"] = "paskutinis is triju"

def tell_a_joke():
    label_pasirinkta["text"] = "this isn't funny"

def fart():
    label_pasirinkta["text"] = "piiirst"
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f

def callback(url):
    webbrowser.open_new(url)

def launch_url(event):
    url = entry_url.get()
    callback(url)
<<<<<<< HEAD
    label_pasirinkta["text"] = f"Paleidom broswerį su {url}"
=======
    label_pasirinkta["text"] = f"Pasileido {url}"

>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f

meniukas.add_cascade(label="Meniukas", menu=submeniukas)
submeniukas.add_command(label="Pirmas", command=pirmas)
submeniukas.add_command(label="Antras", command=antras)
submeniukas.add_separator()
<<<<<<< HEAD
submeniukas.add_command(label="Trečias", command=trecias)
=======
submeniukas.add_command(label="Trecias", command=trecias)
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f

meniukas.add_cascade(label="Fun", menu=submeniukas2)
submeniukas2.add_command(label="Tell a joke", command=tell_a_joke)
submeniukas2.add_command(label="Fart!", command=fart)

meniukas.add_cascade(label="Settings", menu=submeniukas3)
submeniukas3.add_radiobutton(label="Setting 1")
submeniukas3.add_radiobutton(label="Setting 2")

<<<<<<< HEAD
label_iveskite_adresa = Label(langas, text="Enter URL:")
entry_url = Entry(langas)
langas.bind("<Return>", launch_url)

label_pasirinkta = Label(langas, text="...kolkas nieko...", bd=10, relief=SUNKEN, anchor=W)
label_pasirinkta.pack(side=BOTTOM, fill=X)
label_iveskite_adresa.pack(side=TOP)
entry_url.pack(side=TOP)

langas.mainloop()
=======
label_iveskite_adresa = Label(langas, text="Enter URL: ")
entry_url = Entry(langas)
langas.bind("<Return>", launch_url)

label_pasirinkta = Label(langas, text="...kol kas nieko", bd=2, relief=SUNKEN,  anchor=N) # bd = borderwidth, relief = idubimas, anchor - lygiavimas
label_pasirinkta.pack(side=BOTTOM, fill=X)
label_iveskite_adresa.pack(side=TOP)
entry_url.pack(side=TOP)
langas.mainloop()

>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
