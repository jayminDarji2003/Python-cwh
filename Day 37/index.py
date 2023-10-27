# Finally keyword.
# In the interview, if interviewer will ask what is the use of Finally keyword ?. 
# Answer is : The finally block always executes whether the program return or not.

# let's see from example
def mulTable(n):
    try:
        print(f"Multiplication table of {n} is ")
        n = int(n)
        for i in range(1,11):
            print(f"{n} X {i} = {n*i}")
        return "Done with multiplication table"
    except:
        print("Error occurred while creating multiplication table")
    finally:
        print("I am always executed")


# ans = mulTable(6) # not raise error
ans = mulTable("jaymin") # raise error
print(ans)