# "is" vs "==" operator

# is
# "is" is a identity operator.
# is works on objects location
# == works on object value

a = "4"
b = 4

print(a == b)  # false
print(a is b)  # false

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)  # true
print(l1 is l2)  # false
