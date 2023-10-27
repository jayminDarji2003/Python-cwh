# LOCAL VS GLOCAL VARIABLES.

x = 100
# print(x)


def hello():
    global x
    x = 909
    print(f"The local x is {x}")
    print("Hello jayu")


print(f"The global x is {x}")
hello()
print(f"The global x is {x}")
