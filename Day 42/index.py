# Enumerate function in python.
# Enumerate function is very useful when performing loop in sequence. Enumerate function give us index and value of sequence.
# Before enumerating function we have to specify the index and increment the index but enumerate function solve this problem.

# let's see through example
fruits = ["Banana", "Apple", "Orange", "Watermelon", "Muskmelon"]

# we want that when 2nd index comes loop will terminate or print something.

for index, fruit in enumerate(fruits):
    print(fruit)
    if index == 2:
        print("Thanks for playing!!")
        break
