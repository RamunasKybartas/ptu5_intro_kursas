from tkinter import *
from PIL import ImageTk, Image

langas = Tk()
<<<<<<< HEAD
tiltas = ImageTk.PhotoImage(Image.open("img/pont_au_mousson.jpg"))
panel = Label(langas, image=tiltas)
=======
operatoriai = ImageTk.PhotoImage(Image.open("img\\loginiai_operatoriai.png"))
panel = Label(langas, image=operatoriai)
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
panel.pack(side=BOTTOM, fill=BOTH, expand=YES)
langas.mainloop()
