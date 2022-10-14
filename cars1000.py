import sqlite3


connector = sqlite3.connect('SQL/cars1000.db')
cursor = connector.cursor()

insert_query = '''
INSERT INTO cars VALUES
(?,?,?,?,?)
'''
search_query = '''
SELECT * FROM cars
WHERE
make LIKE ?
AND
model LIKE ?
AND
color LIKE ?
AND
year BETWEEN ? AND ?
AND
price BETWEEN ? AND ?
'''

def insert():
    make = input('Make: ')
    model = input('Model: ')
    color = input('Color: ')
    year = int(input('Year: '))
    price = int(input('Price: '))
    with connector:
        cursor.execute(insert_query, (make, model, color, year, price))
    print(f'{make} {model} ({year}) successfully created!')

def search():
    make = input('Make: ')
    model = input('Model: ')
    color = input('Color: ')
    year_from = input('Year from: ')
    year_to = input('Year to: ')
    price_from = input('Price from: ')
    price_to = input('Price to: ')
    search_tuple = (
        make + '%' if make else '%',
        model + '%' if model else '%',
        color + '%' if color else '%',
        int(year_from) if year_from else 1900,
        int(year_to) if year_to else 2022,
        int(price_from) if price_from else 0,
        int(price_to) if price_to else 100000
    )
    
    with connector:
        cursor.execute(search_query, search_tuple)
        res = cursor.fetchall()
        
    for i in res:
        print(i)
    print(f'\nTotal {len(res)} cars found.')

while True:
    choice = input('Search, Insert or Quit? (s/i/q): ')
    if choice == 's':
        search()
    elif choice == 'i':
        insert()
    elif choice == 'q':
        print("Quitting")
        exit()
    else:
        print('Input s, i or q!')
