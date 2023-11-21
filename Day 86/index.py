# Walrun operator in python.

# simple example
a = True
print(a := False)

# second example
myList = [1,2,3,4,5,6,7,8,9]

while (n := len(myList)) > 0:
    print(myList.pop())

print(myList)