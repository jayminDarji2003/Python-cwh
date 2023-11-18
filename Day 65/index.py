# Static methods in python 
# The static method is one type of method which is created inside the class but not belongs to instance or class.

class Math:
    @staticmethod
    def add(a,b):
        return a+b
    
sum = Math.add(10,20)
print(f"The sum of two numbers is : {sum}")