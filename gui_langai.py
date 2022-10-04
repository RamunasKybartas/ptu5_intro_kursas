import tkinter as tk


class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.b_naujas_langas = tk.Button(
            self.master, 
<<<<<<< HEAD
            text="Naujas \U0001F680 Langas", 
            width=20, 
            command=self.new_window, 
            font=sriftas, 
            fg='#fc0', 
            bg='#630', 
        )
        self.b_naujas_langas.bind("<Enter>", lambda e: self.on_enter())
        self.b_naujas_langas.bind("<Leave>", lambda e: self.on_leave())
        self.b_naujas_langas.pack()

    def on_enter(self):
        self.b_naujas_langas['bg']='#741'
        self.b_naujas_langas['fg']='#fd2'
    
    def on_leave(self):
        self.b_naujas_langas['bg']='#630'
        self.b_naujas_langas['fg']='#fc0'
=======
            text="\U0001F680naujas langas", 
            width=40, command=self.new_window, 
            font=sriftas, 
            fg="#900", 
            bg="#00f",
            highlightbackground="#005",
            highlightcolor="#fd2"
            )
        self.b_naujas_langas.bind("<Enter>", lambda e: self.on_enter())  
        self.b_naujas_langas.bind("<Leave>", lambda e: self.on_leave())  
        self.b_naujas_langas.pack()  
    
    def on_enter(self):
        self.b_naujas_langas["bg"] = "#741"

    def on_leave(self):
        self.b_naujas_langas["bg"] = "#00f"

>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f

    def new_window(self):
        self.vidinis = tk.Toplevel(self.master)
        self.app = Vidinis(self.vidinis)

<<<<<<< HEAD
class Vidinis:
    def __init__(self, master):
        self.master = master
        self.b_uzdaryti = tk.Button(self.master, text="\u2717 Uždaryti", width=10, command=self.close_window, font=sriftas, fg='#f00')
        self.b_uzdaryti.pack()

    def close_window(self):
        self.master.destroy()

print("\U0001F680")
langas = tk.Tk()
sriftas = "Roboto", 20, "normal"
=======



class Vidinis:
    def __init__(self, master):
        self.master = master
        self.b_uzdaryti = tk.Button(self.master, text="\U0001F61C uzdaryti", width=10, command=self.close_window, font=sriftas, fg="#f00")
        self.b_uzdaryti.pack()
    def close_window(self):
        self.master.destroy()

langas = tk.Tk()
sriftas = ("Comic Sans MS", 10, "bold")
>>>>>>> e8b3520afa44ff27cd38e5518a508a1c7cb43b4f
programa = Pagrindinis(langas)
langas.mainloop()
