# Generators in python

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator to get the first 10 Fibonacci numbers
for number in fibonacci_generator(10):
    print(number)
