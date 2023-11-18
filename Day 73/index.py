# Dunder method in python
"""
    __init__
    __len__
    __str__
    __repr__
    __call__
"""

class Employee:
    name = "jaymin"

    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"The name of the employee is {self.name}"
    
e = Employee()
print(len(e))
print(e)
