# Constructor in python
# Constructor is nothing but a function which is called automatically when the object is created.It is used to set instance properties.
"""
    Types of constructor
        1. Default constructor ->doesn't accept argument
        2. Parameterized constructor -> accept argument
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)


a = Person("Ankit", 39, "Man 🙍‍♂️")
p = Person("Pooja", 29, "female 🙍‍♀️")

a.info()
print("--------------------------------")
p.info()
