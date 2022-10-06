# def poriniai():
#     skaicius = 2
#     while True:
#         yield skaicius
#         skaicius += 2
        
# skaiciuojam = poriniai()

# for skaicius in skaiciuojam:
#     print(skaicius)

# skaiciuojam = poriniai()
# while True:
#     print(next(skaiciuojam))
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. Parašykite generatorių, kuris tikrins po viena kombinaciją, pradedant 0000, 
# ir sustos, kai pin kodas bus teisingas. Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau. Pabaigus funkciją, praiteruokite 
# sukurtą generatorių su for ciklu, kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį, parašytų 'PIN is XXXX(jųsų pin'as)'. Atkreipkite
#  dėmesį, kad kodas gali prasidėti nuliu. Sugalvokite, kaip apeiti šią problemą (hint - type conversion, if sąlygos).
# kodas = "0989"

# def kodo_tikrinimas():
#     spejimas = 0
#     while True:
#         yield spejimas
#         if spejimas == int(kodas):
#             if len(str(spejimas)) < 4:
#                 if len(str(spejimas)) == 3:
#                     print(f'PIN is 0{spejimas}!')
#                 elif len(str(spejimas)) == 2:
#                     print(f'PIN is 00{spejimas}!')
#                 else:
#                     print(f'PIN is 000{spejimas}!')
#             else:
#                 print(f'PIN is {spejimas}!')
#             break
#         spejimas += 1
       
# kodukas = kodo_tikrinimas()
# while True:
#     print(next(kodukas))
# for numeris in kodukas:
#     print(numeris)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# counter = (f"{num:04}" for num in range(10000))
# pin_list = list(counter)
# for pin in pin_list:
#     print(pin)
#     if pin == "0549":
#         print(f"PIN kodas yra: {pin}")
#         break

# number = 20
# print(f"{number:04}")

# PIN = '0099'

# def pin_breaker(pin):
#     guess = 0
#     while True:
#         res = ("0" * (4 - (len(str(guess))))) + str(guess)
#         if res == pin:
#             print(f"PIN is {res}")
#             break
#         yield res
#         guess += 1


# generator = pin_breaker(PIN)

# for num in generator:
#     print(num)
# -------------------------------------------------------------------------------------------------------------------------------------------------


# Parašykite generatoriaus funkciją, kuri atidarytų nurodytą failą, ir grąžintų po vieną 
# eilutę (tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.). Reikės prisiminti darbą su failais :)


# def skaitom_faila(failas, zodis):
#     with open(failas, "r") as skaitom:
#         for eilute in skaitom:
#                 yield  eilute
#                 if zodis in eilute:
#                     break
 

# bandom = skaitom_faila("c:\\codeacademy\\beginner_ending\\tekstas.txt", "acuteness")
                                       
# for x in bandom:
#     print(x)
# --------------------------------------------------------------------------------------------------------------------

# class Myiter:
#     def __init__(self, number):
#         self.number = number

#     def __iter__ (self):
#         self.n = 1
#         return self

#     def __next__ (self):
#         if self.n <= self.number:
#             result = self.n ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration 


# for i in Myiter(5):
#     print(i)

class Testas:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42
t = Testas()
print(dir(t))
print(t._Testas__baz)