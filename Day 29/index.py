# DocStrings 
# Docstring is written to explain how function,class,module works.
# It is not a comment but it is similar to a comment.

def square(n):
    ''' Takes in a n, returns the square of n '''
    print(f"sqare of {n} is = ",n**2)

square(5)
print(square.__doc__)

print("---------------------------------------")

# Print Zen of python.
import this