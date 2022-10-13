class Vehicle:
    # class variable - nekintama visoms inherited klasems
    color="white"
    # instance variable (__init__) tik priskiriamos klases variables
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

    def __repr__(self):
        return f"pavadinimas: {self.name}, max greitis: {self.max_speed}, pravaza: {self.mileage} ir spalva - {self.color}"

    def seating_capacity(self, capacity):
        return f"seating capacity of {self.name} is {capacity} passengers"

    def fare(self, capacity):
        self.ammount = capacity * 100
        return f"tvarkymo kaina masinai {self.name} - {capacity * 100} eur"


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50, color="green"):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity
        self.color = color

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        return f"tvarkymo kaina masinai {self.name} - {self.capacity * 110} eur"

class Car(Vehicle):
    color = "brown"
    pass


class MiniBus(Bus):
    pass

auto1 = Vehicle("Ford Ka", 200, 2102101)
auto2= Bus("Big yellow Volvo", 120, 210100)
auto3 = Car("Small BMW", 200, 150000)
auto4 = MiniBus("Mini busiukas", 75, 90000, "Pink")
# print(auto2.seating_capacity())
# print(auto1.seating_capacity(5))
print(auto1)
print(auto2)
print(auto3)
print(auto4)
print(auto1.fare(5))
print(auto2.fare())
