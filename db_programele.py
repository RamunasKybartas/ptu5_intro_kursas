import sqlite3
from pprint import pprint

connector = sqlite3.connect("SQL/cars.db")
cursor = connector.cursor()

with connector:
    while True:
        ivedimas = input("Iveskite auto paieskai arba ! kad iseiti arba '.', kad ivesti auto: ")
        if ivedimas == "!":
            break
        elif ivedimas == ".":
            print("___NEW CAR___")
            new_make = input("Make: ")
            new_model = input("Model :")
            new_color = input("Color :")
            new_year = input("Year of a car: ")
            new_price = input("Price of a car: ")
            cursor.execute('INSERT INTO cars (make, model, color, year, price) VALUES (?, ?, ?, ?, ?)', 
                (new_make, new_model, new_color, new_year, new_price, ))
            connector.commit()
            print("Car added sucsessfully")
        else:
            select_query = 'SELECT * FROM cars WHERE make LIKE ?'
            cursor.execute(select_query, (f'%{ivedimas}%', ))
            rezultatas = cursor.fetchall()
            if rezultatas:
                print(f"Rasti automobiliai:")
                for auto in rezultatas:
                    print(f"{auto[:3]}, kaina: {auto[4]} $")
            else:
                print("Tokios auto nera")
    print("Iki")

