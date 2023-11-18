# super() method in python
# If we want to access the parent class method from the child class then the super() method used.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showData(self):
        print("--------- parent method called -------")
        print(self.name)
        print(self.age)


class jayu(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.height = "6.5m"
        self.weight = "55kg"

    def showData(self):
        super().showData()
        print("--------- child method called -------")
        print(self.height)
        print(self.weight)


j = jayu("jaymin", 20)
j.showData()
