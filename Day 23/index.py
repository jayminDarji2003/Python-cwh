# List methods

myList = [11,2,3,42,52,6,7,8,9,10,10,10]
print("Original list = ",myList)

# append() method
myList.append(999)
print("Perform append method = ",myList)

# sort() method
myList.sort() # sort in ascending order
print(myList) 

myList.sort(reverse=True) # sort in decending order
print(myList) 

# reverse() method
myList.reverse()
print(myList)

# index(element) 
# This method returns the index of the element
print(myList.index(10))

# count() method
# This method returns count of number of items with the given value
print(myList.count(10))

# copy() method
# This method copies the list in memory
l1 = [1,2,3,4,5]
l2 = l1.copy()
print(l1, id(l1))
print(l2, id(l2))

# insert() method
# When we want to insert value in a given index then this method used.
myList.insert(4,9000182)
print(myList)

# extend() method
# This method adds two list. Also called concate of two lists.
myList.extend(l1)
print(myList)