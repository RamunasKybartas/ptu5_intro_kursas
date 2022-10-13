# class Mokinys:
#     def __init__(self, vardas, pavarde, amzius=18):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius

#     def __str__(self) -> str:
#         return f"studento vardas {self.vardas}, pavarde {self.pavarde}, ir jo amzius: {self.amzius}"

#     def mokinti(self):
#         return f"{self.vardas} mokinasi"

# mokinys = Mokinys("Rokas", "Balsys")
# print(mokinys)
# print(mokinys.__dict__)
# print(Mokinys.mokinti(mokinys))


# class Funkcija:
#     def __init__(self, number):
#         self.number = number

#     def abs(self):
        
#         print(abs(self.number))

# x = Funkcija(-20)
# x.abs(-20)

# def mokinys(*args):
#     for zodis in args:
#         yield f"elementas {zodis}"
      

# zodziai = mokinys("tas", "anas", "toks")

# print(next(zodziai))
# print(next(zodziai))
# print(next(zodziai))


# class Student:
#     pass

# class Marks:
#     pass


# mokinys = Student()
# pazymys = Marks()

# print(pazymys.__class__)
# print(isinstance(mokinys, Student))
# print(isinstance(mokinys, object))
# print(issubclass(Student, mokinys))


# class Student:
#     student_name = "Terrence Ross"
#     marks = 75

# setattr(Student,"student_class", "good")
# print(getattr(Student, "student_name"))
# print(getattr(Student,"student_class"))
# print(Student.marks)
# delattr(Student, "marks")

# print(f"name of the person: {getattr(Student, 'student_name')}")
# print(Student.__dict__.values())

# class Student:
#     student_id = 895621
#     student_name = "Terrencce Ross"

#     def give_items():
#         print(f"{Student.student_id} and {Student.student_name}")



# Student.give_items()
# setattr(Student, "height", "185")
# print(Student.__dict__)

# roman - integer konvertuotojas
# class Converter:

#     def konvertuojam(self, number):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  number > 0:
#             for _ in range(number // val[i]):
#                 roman_num += syb[i]
#                 number -= val[i]
#             i += 1
#         return roman_num


# print(Converter().konvertuojam(95))


# class gaunam:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))
    
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
#         return [current]

# print(gaunam().sub_sets([1,2,3]))


# class Rectangle():
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def calc(self):
#         return self.width * self.length

# rect = Rectangle(10, 20)

# print(rect.calc())
# ---------------------------------------------------------------------
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         return 2*3.14*self.radius

#     def area(self):
#         return 3.14*(self.radius*self.radius)
        

# sirkl = Circle(8)

# print(sirkl.area())
# print(sirkl.perimeter())

# class Stringai:
#     def __init__(self):
#         self.string = ''

#     def get_string(self):
#         self.string = input("enter a string: ")


#     def print_string(self):
#         return self.string.upper()


# str = Stringai()
# str.get_string()
# print(str.print_string())



# ____________________________________________________________________________________________________________________


# class Skaiciai():

#     def paimam_dauginam(self):
#         self.str = input("iveskite ")
#         try:
#             self.sk = int(input("iveskite "))
#         except ValueError:
#           print(f"turi buti skaicius!")
        
    
#     def dauginam(self):
#         try:
#             return self.str * self.sk
#         except Exception as e:
#             print(f"negalima dauginti raidziu is raidziu, klaida: {e}")


# stringas = Skaiciai()
# stringas.paimam_dauginam()
# print(stringas.dauginam())

# ------------------------------------------------------------------------------------------------------

# class Zodziai:
#     def verciam(self, stringas):

#         print(stringas.split()[::-1])


# Zodziai().verciam("labas ka tu")

# class FindPair():
#     def __init__(self, listas, target):
#         self.target = target
#         self.listas = listas
#     def calc(self):
#         i = 0
#         for i, x in enumerate(self.listas):
#             if x < self.target:
#                 j = 0
#                 for j, number in enumerate(self.listas):
#                     if x + number == self.target:
#                         return (f"{x} {number} ir indeksai: {i} {j}")
#                     j +=1
#             i +=1        
                        

# bandymas = FindPair([10,20,10,40,50,60,70], 130)
# print(bandymas.calc())


# 6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. Go to the editor
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


# class Finsum():
#     def __init__(self, list):
#         self.list = list

#     def findzero(self):
#         for x in self.list:
#             for y in self.list:
#                 for z in self.list:
#                     if x+y+z == 0:                       
#                         print(x,y,z)


# bandom = Finsum([-25, -10, -7, -3, 2, 4, 8, 10])
# bandom.findzero()


# class py_solution:
#  def threeSum(self, nums):
#         nums, result, i = sorted(nums), [], 0
#         while i < len(nums) - 2:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#             i += 1
#             while i < len(nums) - 2 and nums[i] == nums[i - 1]:
#                 i += 1
#         return result

# print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

