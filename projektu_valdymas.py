from sqlalchemy.orm import sessionmaker
from projekto_modelis import Projektas, engine


session = sessionmaker(bind=engine)()

def print_projects():
    print("---Projektai---")
    print("#, Pavadinimas, Kaina, Sukurta")
    projects = session.query(Projektas).all()
    for project in projects:
        print(project)

def new_project():
    print("---Naujas Projektas---")
    try:
        name = input("Pavadinimas: ")
        price = float(input("Kaina: "))
    except ValueError:
        print("Klaida: kaina turi buti skaicius: ")
        return None
    else:
        project = Projektas(name, price)
        session.add(project)
        session.commit()
        print(f"Projektas {project} sukurtas sekmingai!")


def input_project():
    print_projects()
    try:
        project_id = int(input("Iveskite pasirenkamo projekto id: "))
    except ValueError:
        print("KLAIDA: ID turi buti skaicius")
        return 
    else:
        return project_id

def update_project():
    project_id = input_project()
    if project_id:
        project = session.query(Projektas).get(project_id)
        if project:
            try:
                name = input(f"Pavadinimas ({project.name}): ")
                price = float(input(f"Kaina: ({project.price}): ") or 0) # jeigu neivedama  tada defaultine reiksme nulis
            except ValueError:
                print("Klaida: kaina turi buti skaicius.")
                return
            else:
                if len(name) > 0:
                    project.name = name
                if price:  #tikrinam ar kaina ivesta ir ne nulis (True salyga 1 ir daugiau)
                    project.price = price
                session.commit()
                print(f"Projektas {project} atnaujintas sekmimgai")
        else:
            print(f"Projektas su ID {project_id} neegzistuoja")

def delete_project():
    project_id = input_project()
    if project_id:
        trinamas = session.query(Projektas).get(project_id)
        if trinamas:
            session.delete(trinamas)
            session.commit()
            print(f"Projektas {trinamas} istrintas sekmingai!")
        else:
            print(f"KLAIDA: projektas su tokiu ID neegzistuoja")


while True:
    print("==Projektu valdymo duomenu baze==")
    print("Galimi pasirinkimai: ")
    print("-q: iseiti")
    print("-r: rodyti visus projektus")
    print("-n: naujas projektas")
    print("-u: pakeisti projekto duomenis")
    print("-d: trinti projekta")
    pasirinkimas = input("Pasirinkite: ").casefold()
    if pasirinkimas == "q":
        break
    elif pasirinkimas == "r":
        print_projects()
    elif pasirinkimas == "n":
        new_project()
    elif pasirinkimas == "u":
        update_project()
    elif pasirinkimas == "d":
        delete_project()
    else:
        print("blogas pasirinkimas, ne ta raide")


