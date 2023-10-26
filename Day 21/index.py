# Types Arguments in functions
"""
    There are four types of arguments
        1. required arguments (normal arguments)
        2. Keyword arguments
        3. Defualt arguments
        4. Arbitrary arguments
"""


def average(a, b, c=90):
    print("The average of numbers is : ", (a + b + c) / 3)


# 1. required arguments (normal arguments)
average(10, 20, 30)

# 2. Keyword arguments
average(a=10, b=20, c=30)

# 3. Defualt arguments
# third argument already given
average(10, 20)

# 4. Arbitrary arguments
def sum(*elements):
    print(elements)
    sum = 0
    for i in elements:
        sum += i
    return sum

ans = sum(10, 20, 30, 40, 50)
print(ans)

print("--------------------------------")

# send data as dictionary
def names(**name):
    print(type(name))
    print(name)

names(fname="Darji",mname="Jaymin",lname="Satishkumar")