# slicing and operations on strings
names = "jaymin,deep"
print(len(names))  # length of the string

# slicing
print(names[0:6])  # start 0 and goes to 6, remember 6 is not inclusive
print(names[6:])  # start from 6 and goes to end of the string
print(names[:4])  # it is automatically include start of 0 and goes to 4 index
print(
    names[3:-1]
)  # it is very important to know that is is start from 0 and goes to --> len(names) - 1 index.
print(
    "name is : ", names[-7:9]
)  # is is same as above it start from --> len(names) - 7 index and goes to 9 index.


# loop through string
myName = "Pradip Mehra"
for i in names:
    print(i)


# Quick Quiz
nm = "harry"
print("Quick quiz ans : ", nm[-4:-2])
