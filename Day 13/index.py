# Strings methods
# Note : strings are immutable
a = "jaymin"
print(a)

# get length
print(len(a))

# convert to uppercase
print(a.upper())

# convert to lowercase
print(a.lower())

# convert to capitalized case
a2 = "jaymin darji"
print(a2.capitalize())

# remove leading and trailing whitespace/char
str = "deep!!!!"
print(str.rstrip("!"))

# replace string
pst = "this is jaymin"
new_pst = pst.replace("jaymin", "kishan")
print(new_pst)

# split method
# this method is used to split a string into a list of strings
my_str = "this is jaymin and he is a greate programmer"
split_string = my_str.split(" ")
print(split_string)
print(type(split_string))

# center method
# this method is used to center a string into a list of strings
myStr = "I'm a greate programmer"
print(myStr)
print(len(myStr))
print(myStr.center(50))
print(len(myStr.center(50)))

# count method
# this method is used to count a string into a list of strings
s = "countii string"
print(s.count("ti"))

# endswith method
# this method tell us, if the string ends with a perticular string or character
b = "this string is endswith !!!"
print(b.endswith("!!!"))
print(b.endswith("!!!!"))

# find method
# it finds first occurrence of a string in a list of strings
a = "this is string is created by string"
print(a.find("string"))

# index method
# similar to find method, but it finds the first occurrence