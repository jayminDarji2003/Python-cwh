# class and object in python


# creating class
class Teacher:
    name = "Teacher"
    age = 30
    teach = "English"

    def changeName(self, name):
        self.name = name

    def changeAge(self, age):
        self.age = age

    def changeTeach(self, sub):
        self.teach = sub


# creating object
Ankita = Teacher()

# accessing class data
print(Ankita.name)
print(Ankita.age)
print(Ankita.teach)

# accessing class methods
Ankita.changeName("Ankitben")
Ankita.changeAge(89)
Ankita.changeTeach("Maths")

print("--------------------------------")

# accessing class data
print(Ankita.name)
print(Ankita.age)
print(Ankita.teach)
