"""Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti. 
Galite patobulinti, pvz funkcijos (vardas), su tokiais ir tokiais argumentais vykdymo 
laikas - XX s. Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą ir su funkcija, 
išrenkančia pirminius skaičius užduotame diapazone. """


import requests  # importuojame requests
from time import time  # importuojame time modulį

start_time = time()  # fiksuojame starto laiką
r = requests.get('http://www.cnn.com')  # sukuriame http užklausą
# print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes)
end_time = time()  # fiksuojame pabaigos laiką
tikslus = ("%.2f"%(end_time - start_time))
# print(tikslus)  # atspausdiname laiką, per kurį gaovme atsakymą



from functools import wraps
from time import time
import requests


def speed_test(fn):
    # wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        fn(*args, **kwargs)
        end_time = time()
        runtime = end_time - start_time
        print(f"Function's '{fn.__name__}', with given parameters {args} runtime: {round(runtime, 2)}s")
    return wrapper


# @speed_test
# def get_status(website):
#     r = requests.get(website)
#     # print(r.status_code)


# get_status('http://python.org')

@speed_test
def prime_finder(given_range):
    final_list = []
    for num in range(given_range):
        if num > 1:
            for i in range(2,num):  
                    if (num % i) == 0:  
                        break
            else:  
                final_list.append(num)
    return final_list

prime_finder(10000)

