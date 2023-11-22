# Regular Expression in python.
# The Regular Expression is used to perform a match against the strings. If we want to perform a string match cases then regular expression is used.

# First we need to import "re" package

import re


text = """
Python Expressions:
Expressions are representations of value. They are different from statement in the fact that statements do something while expressions are representation of value. For example any string is also an expressions since it represents the value of the string as well.

Python has some advanced constructs through which you can represent values and hence these constructs are also called expressions.

In this tutorial you will get to know about:

What are expressions in Python
How to construct expressions.
How to create an expressions
Python expressions only contain identifiers, literals, and operators. So, what are these?

Jaymin
Paymin
Taymin

Identifiers: Any name that is used to define a class, function, variable module, or object is an identifier. Literals: These are language-independent terms in Python and should exist independently in any programming language. In Python, there are the string literals, byte literals, integer literals, floating point literals, and imaginary literals. Operators: In Python you can implement the following operations using the corresponding tokens.
"""

# pattern is expression we want to search in the text.
# pattern = "and"

# ---------------------------------

# pattern = "Jaymin"  # if exists then return text.
# match = re.search(pattern, text)
# print(match.group())

# ---------------------------------

pattern = r"[A-Z]aymin"  # if exists then return text.

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())
