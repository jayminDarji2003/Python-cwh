# Method overriding in python

class Parent:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print("---- Parent ----")
        print(self.name)

class Child(Parent):
    def __init__(self,name):
        self.name = name
    
    # def display(self):
    #     print("---- Child ----")
    #     print(self.name)

c = Child("Jaymin")
c.display()