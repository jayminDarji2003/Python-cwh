# Introduction to List
"""
    List are : 
        1. Ordered
        2. Mutable
        3. Contains duplicate 
"""
l = [5, 6, 7, 8, 9]
print(l)
print(type(l))

# accessing elements of a list
print(l[0])
print(l[1])
print(l[2])

print("-------------------------")
# Negative indexing
print(l[-1]) # automatically generate => [len(l)-1]

# check if element present in list or not
if 7 in l:
    print("Present in list")
else:
    print("Not present in list")

print("-------------------------------")

# print whole list
print("Printing the list = ",l)

# slicing on list
print("--------- slicing on list -------")
print(l[:])
print(l[1:])
print(l[1:4])
print(l[1:-2])
print(l[1::1])

# List comprehension
print("--------- list comprehension ---- ")

myList = [i for i in range(10)]
print(myList)

myList2 = [i*i for i in range(10)]
print(myList2)

mylist3 = [i for i in range(50) if i%2==0]
print(mylist3) 
