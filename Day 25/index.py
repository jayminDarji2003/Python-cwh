# Tuple methods
# In tuple we can not add,update,delete elements directly because as we know tuple is immutable.But if we want to perform add,update,delete then we need to convert tuple into a list and then perform operations after that convert to tuple

'''

myTup = (1,2,3,4,5,6,7,8)
print("Tuple is = ", myTup)

myList = list(myTup)
print("List is = ",myList)
# add
myList[0] = 99999
print("List is = ",myList)
# remove last element
myList.pop()
print("List is = ",myList)
# remove method
myList.remove(4)
print("List is = ",myList)

myTup = tuple(myList)
print("Tuple is = ",myTup)

'''

# Tuple methods 

myTup = (1,2,3,4,5,6,7,8,1,1)

# count() method
print(myTup.count(1))

# index() method
print(myTup.index(1))

# len() method
print(len(myTup))