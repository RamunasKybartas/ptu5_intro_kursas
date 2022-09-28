from tkinter import *
from PIL import ImageTk, Image

langas = Tk()
operatoriai = ImageTk.PhotoImage(Image.open("img\\loginiai_operatoriai.png"))
panel = Label(langas, image=operatoriai)
panel.pack(side=BOTTOM, fill=BOTH, expand=YES)
langas.mainloop()
