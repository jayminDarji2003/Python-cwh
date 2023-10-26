# Tuple in python
# Tuple in similar to list in some cases.
# Tuple is ordered collections of elements and it is immutable.

tup = (1,2,3,4,5)
print(type(tup), tup)

# accessing elements in tuple
print(tup[2])
print(tup[3])
print(tup[4])

# check elements contains or not
if 8 in tup:
    print("contains")
else:
    print("not contains")

# check same or not
if tup[0] is 1:
    print("same")
else:
    print("not same")


# slicing is same as list