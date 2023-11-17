# Inheritance in python
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def showData(self):
        print(f"The id of the employee is : {self.id}")
        print(f"The name of the employee is : {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")



e1 = Programmer(891, "Rohan das")
e1.showData()
e1.showLanguage()
