# Dictionary methods

ep1 = {101: 45, 102: 89, 894: 89, 33: 90}
ep2 = {110: 89, 120: 89}

# update() method
# used to add two dictionary
ep1.update(ep2)
print(ep1)

# clear() method
# used to remove all the key value pairs from the dictionary
ep2.clear()
print(ep2)

# empty dictionary
# dict = {}
# print(type(dict))

# pop() method
print("--------------------------------------")
for key in ep1.keys():
    print(ep1[key])
print("--------------------------------------")
a = ep1.pop(120)
print(a)

# popitem() method
# remove last key:value pairs
a = ep1.popitem()
print(a)

# del keyword
del ep2
# print(ep2)