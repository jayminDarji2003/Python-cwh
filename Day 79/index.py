# Multiple inheritance
# In multiple inheritance there are several parents but only one child.

class Father:
    def __init__(self, fname):
        self.fatherName = fname

    def displayData(self):
        print(f"Father name is {self.fatherName}")

class Mother:
    def __init__(self, mname):
        self.motherName = mname

    def displayData(self):
        print(f"Mother name is {self.motherName}")


class Child(Father,Mother):
    def __init__(self, fname,mname ,cname):
        self.childName = cname

    def displayData(self):
        print(f"Child name is {self.childName}")


c = Child("Satishkumar", "Naynaben", "jaymin")
c.displayData()

