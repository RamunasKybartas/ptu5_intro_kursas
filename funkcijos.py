# Sukurti funkcijas, kurios:
# Gražintų visų paduotų skaičių sumą (su *args argumentu)
# Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
# Gražintų paduoto sakinio simbolių kiekį (su len())
# Gražintų rezultatą, skaičių x padalinus iš y

import logging

# logging.basicConfig(
#     filename="funkcijos.log", 
#     level=logging.INFO, 
#     format="%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"
# )
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('funkcijos.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


from math import sqrt
from functools import reduce
def suma(*skaiciai):
    sum = reduce(lambda x, y: x + y, skaiciai)
    logger.info(f"funkcijos {suma.__name__} visu {skaiciai} suma yra {sum}")
    return sum
    
def saknys_traukiam(skaicius):
    try:
        saknis = sqrt(skaicius)
    except TypeError as e:
        logger.error(f"funkcijoje {saknys_traukiam.__name__} gavosi klaida {e.__class__.__name__}: {e}")
        return None
    else:
        logger.info(f"Saknis skaiciaus {skaicius} yra {saknis} ")
        return saknis

def sakinys(sakinys):
    ilgis = len(sakinys)
    logger.info(f"Sakinio {sakinys} ilgis yra {ilgis} ")
    return ilgis

def dalinam(x, y):
    try:
        logger.info(f"Skaiciu {x} padalinus is {y} gaunasi {x // y} ")
        return x // y
    except ZeroDivisionError as e:
        logger.error(f"funkcijoje {dalinam.__name__} traukti sakni is {y} negalima, klaida: {e.__class__.__name__} : {e}")
    


print(saknys_traukiam("9"))
print(suma(1, 2, 3, 4, 5, 6, 7))
print(sakinys("laba laba laba ahoy"))
print(dalinam(10, 0))
