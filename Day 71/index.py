# dir() , _dict_() and help() method

"""
    dir() :- the dir() method returns the list of methods which is belongs to the object.

    __dict__ attribute :- the __dict__ attribute is used to return all the instance variables for the class in the form of dictionary.

    help() :- the help() method is used to get the information about the class. 
"""

# dir() method
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listMethods = dir(x)

print("--------------------------------")
for method in listMethods:
    print(method)
print("--------------------------------")

# __dict__ method


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p = Person("jaymin", 19, "male")
print(p.__dict__)


# help() method

# if i want to get information about a person class then
print(help(p))

# if i want to get information about str class then
print(help(list))