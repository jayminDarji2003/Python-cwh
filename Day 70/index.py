# // alternative constructors in python


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f"Person name : {self.name}")
        print(f"Person age : {self.age}")
        print(f"Person gender : {self.gender}")

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1], string.split("-")[2])
    

p1 = Person.fromStr("jaymin-20-male")
p1.show()

