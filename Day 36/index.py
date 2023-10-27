# Exception Handling

# ex. Program to generate multiplication table.
# When user enter invalid content then this program will raise exception
# num = int(input("Enter the number : "))
# print(f"Multiplication table of {num} is : ")

# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")


# If we want to make more efficient then we have handle exceptions.
try:
    num = int(input("Enter the number : "))
except ValueError:
    print("------ Please enter a valid number -----")
    num = int(input("Enter the number : "))

print(f"------- Multiplication table of {num} ---------")
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")



'''
    Types of exceptions :
        1. TypeError
        2. ValueError
        3. NameError
        4. ZeroDivisionError
        5. KeyError
        6. ModuleNotFoundError
        7. IndexError
'''