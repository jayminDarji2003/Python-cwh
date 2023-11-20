# single inheritance
# In the single inheritance there are one parent and one child or more child

class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Parent name is : {self.name}")
        print(f"Parent age is : {self.age}")

class Child(Parent):
    def __init__(self,name,age,motherName):
        super().__init__(name,age)
        self.motherName = motherName

    def show(self):
        super().show()
        print(f"Mother name is : {self.motherName}")


c = Child("Satishkumar", 60 , "Naynaben")
c.show()

