# oop

# class,objects,attributes,methods,constructor
# encapsulation
# inheritance
# abstraction
# polymorphism


# # class,objects,attributes,methods,constructor
# class Player:
#     passing = 40  # class attribute
#     defending = 40  # class attribute
#     finishing = 40  # class attribute
#     dribbling = 40  # class attribute
#     goalkeeping = 40  # class attribute

#     def __init__(self, name):  # constructor
#         self.name = name  # object attribute
#         self.passing = 70  # overwrite class attribute

#     def show_details(self):  # self method ma pass garaunai parxa
#         print(self.name)
#         print(self.passing)
#         print(self.defending)
#         print(self.finishing)
#         print(self.dribbling)
#         print(self.goalkeeping)


# ramos = Player("Ramos")
# ramos.show_details()


# inheritance
class People:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    # @property  # decorator = helps to call age() as attribute "age"
    def age(self):
        current = 2025
        return current - self.dob


class Player(People):
    def __init__(self):
        pass


ram = Player("Ram", 2004)
print(ram.name)
print(ram.age())
