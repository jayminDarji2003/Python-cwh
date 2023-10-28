# map, filter, reduce functions

# map
# li = [2, 5, 7, 3, 9]
# newList = list(map(lambda x: x * x, li))
# print(newList)

# filter
# l = [2, 4, 3, 1, 7, 4, 9, 1]
# data = list(filter(lambda x: x % 2 == 0, l))
# print(data)


# reduce
from functools import reduce

l = [2, 4, 3, 1, 7, 4, 9, 1]
ans = reduce(lambda x,y: x+y, l)
print(ans)  
