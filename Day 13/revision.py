# Strings are immutable, we can't change or modify it.If we change or modify it will generate new string.

a = "jaymin"

# find length
print("Length of string = ", len(a))

# convert to uppercase
print("Uppercase string = ", a.upper())

# convert to lowercase
print("Lowercase string = ", a.lower())

# rstrip() method
# The rstrip() method removes trailing characters from a string.
s = "Hello !!!"
print("rstrip() method = ", s.rstrip("!"))

# replace() method
a = "Hello jaymin, how are you?"
print("replace() method = ", a.replace("jaymin", "Het"))

# split() method
# The split() method convert a string to list.
a = "Hello world"
print("split() method = ", a.split(" "))

# capitalize() method
# The capitalize method is used to convert first character of the sentence to upppercase and other characters convert to lowercase.
title = "introduction to python with Zero to Hero."
print("Capitalize() method = ", title.capitalize())

# center() method
# The center() method is used to aligh string to center.
# Inshort center() method puts spaces before the string as given in parameter.
str = "Jaymin darji from nardipur"
print(str.center(50))

# count() method
# The count method is used to count the character in the string.
str = "Jaymin Darji"
n = str.count("a")
print("The count = ", n)

# endswith() method
# The endswith method is used to check if the string ends with a given value.
str = "Hello jaymin !!!"
print("---------------- endswith method ----------------")
print(str.endswith("!!!"))
print(str.endswith("."))

# find() method
# This method just return the index of first occurrence of the string.
str = "He's name is Den"
print("Find method = ", str.find("is"))
print("Find method = ", str.find("iss"))

# index() method
# This method is same as find() method but in this method given string not found in string then return exception.
str = "He's name is Den"
print("Index method = ", str.index("is"))
# print("Index method = ",str.index("iss"))

# isalnum() method
# This method check if the string consist of alphabat(A-Z or a-z) or number(0-9). If present then return true. If other character present return false.
str = "MyNameIsDen"
print("isalnum() method = ", str.isalnum())

# is alpha() method
# This method check if the string consist only alphabat(A-Z or a-z). If present then return true or false.
str = "MyNameIsDen"
print("isalpha() method = ", str.isalpha())

# islower() method
# Check if string is lower or not.If lower return true otherwise false.
str = "i'm lower string"
print("islower() method = ", str.islower())

# isprintable() method
# returns True if string is printable otherwise False.
str = "i'm printable string"
str2 = "i'm printable string\n"
print("isprintable() method = ", str.isprintable())
print("isprintable() method = ", str2.isprintable())

# isspace() method
# This method returns True if you use white space only in the string, else return False.
str = "     "
print("isspace() method = ", str.isspace())

# istitle() method 
# This method returns True if first character of all the word of the string will be in capitalized, else return False.
str = "World Wide Web"
print("istitle() method = ", str.istitle())

# swapcase() method
# This method converts uppercase character to lowercase and lowercase character to uppercase.
str = "World Wide Web"
print("swapcase() method = ", str.swapcase())

# startswith() method
# This method check if the string start with given word or not. If start with given word return True, else return False.
str = "World Wide Web"
print("startswith() method = ", str.startswith("World"))

# title() method
# This method convert the string into title.
str = "his name is manish, and he is working as a python developer."
print("title() method = ", str.title())

