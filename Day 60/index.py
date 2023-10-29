# Getters and Setters in python 
'''
    There are three types of methods in class
        1. Instance methods
            a. Accessor methods --> Getters
            b. Mutator methods  --> Setters
        2. class methods
        3. static methods
'''

class KIRC:
    def __init__(self,department,noofstu,nooffec):
        self.department = department
        self.noofstu = noofstu
        self.nooffec = nooffec
    
    # getter
    def getData(self):
        print(f"The department is {self.department}")
        print(f"The no of students is {self.noofstu}")
        print(f"The no of feculties is {self.nooffec}")
    
    # setter
    def setData(self, d,s,f):
        self.department = d
        self.noofstu = s
        self.nooffec = f

a = KIRC("BCA", 120, 7)
a.getData()
a.setData("MBA", 90, 10)
print("--------------------------------")
a.getData()



