# Recursion in python
# When function is called itself is called recursion.
def fact(n):
    # base case
    if n == 1 or n == 0:
        return 1
    else:
        return (n * fact(n - 1))


print("Factorial of 6 is = ", fact(6))
