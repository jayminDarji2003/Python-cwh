# Access modifires in python
# Public :- We can access from anywhere in the class or outside of the class.
# ex. --->  self.name = "jaymin darji"
# Access ---->  obj.name

# Private :- We can access the variable only in the class but not outside of the class.
# ex. --->  self.__name = "jaymin darji"
# Access ---->  It is not access directly but we can access through one way.
#  obj._ClassNam.__name

# Protected :- We can access the variable in the class or in the inherited class (child class)
# ex. --->  self._name = "jaymin darji"
# Access ---->  obj._name


class College:
    def __init__(self):
        # public variable
        self.name = "KIRC KALOL"
        self.course = "BCA"
        # private variable
        self.__revenue = 100000
        # protedcted
        self._ceo = "jaymin darji"


class Student(College):
    def disData(self):
        # accessing public variable
        print(self.name)
        print(self.course)

        # accessing protected variable
        print(self._ceo)

st = Student()
st.disData()

# accessing private variable
print(st._College__revenue)
