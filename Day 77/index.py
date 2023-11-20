# Operator overloading

class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,other):
        return f"{self.i + other.i}i + {self.j + other.j}j + {self.k + other.k}k"


v1 = Vector(1,2,3)
print(v1)

v2 = Vector(10,20,30)
print(v2)

print("Addition = " + (v1 + v2))