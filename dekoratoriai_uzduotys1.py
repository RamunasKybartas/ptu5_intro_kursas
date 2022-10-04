# Parašykite dekoratorių kuris riboja parametrų kiekį (tarkime, ne daugiau negu 2 parametrai funkcijai)
# 1.5 Parašykite dekoratorių, kuris atideda funkcijos vykdymą 3s
# Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string tipo parametrus.

from time import sleep

def tik_skaiciai(func):
    def wrapper(*args):
        for i in args:
            if type(i) != int and type(i) != float:
                print(f"tik skaiciai, ivedet: {i}")               
        return func(*args) 
    return wrapper



def paveluojam(sekundes):
    def paveluojam(func):
        def wrapper(*args):
            sleep(sekundes)
            print(f"praleidom {sekundes} sekunde")
            return func(*args)
        return wrapper
    return paveluojam

def args_kiekis(func):
    def wrapper(*args):
        if len(args)>2:
            print("turi buti du argumentai")
            return func(args[0], args[1])
        return func(*args)
    return wrapper


@tik_skaiciai
@args_kiekis
@paveluojam(1)
def bandomoji_funkcija(*args):
    return args[0] * args[1]

print(bandomoji_funkcija(10, 8, "a", "b", "w"))


