import numpy as np

def tikrinam(skaicius):
    for x in range(2, skaicius):
        if skaicius%x==0:
            return False
    return True 

kintamasis = np.arange(1, 101)
print(kintamasis)
funkcija = np.vectorize(tikrinam)
print(kintamasis[funkcija(kintamasis)])

# def tikrinam_dar(nampai):
#     for skaicius in nampai:
#         i = 0
#         for x in range(1, skaicius):
#             if skaicius%x == 0:
#                 i += 1
#         if i==1:
#             return True
#         return False