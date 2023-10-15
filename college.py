# exp = input("Enter the expression : ")
# ans = float(eval(exp))
# print("The ans of the expression is : %.2f" % ans)
# print("The ans of the expression is : ", ans)

# search element in the list


def search(element, item):
    for i in element:
        if i == item:
            return True
    return False


list_new = [1, 2, "het", 5, "heta", "kishan"]
ele = "het"
ans = search(list_new, ele)
if ans:
    print("found", ele)
else:
    print("no found")


# import numpy

# # array
# arr = numpy.array([1,2,3,4,5])
# print(type(arr))

# new_arr = []
# new_arr[:] = arr
# print(type(new_arr) , new_arr)


import numpy as np

# Create the original array
original_array = np.array([1, 2, 3, 4, 5])

# Create a new array from the original array
new_array = original_array.copy()

# You can also create a new array with a modified version of the original array
# For example, let's add 10 to each element of the original array to create the new array
new_array_modified = original_array + 10

# Print the arrays
print("Original Array:", original_array)
print("New Array (Copied):", new_array)
print("New Array (Modified):", new_array_modified)
