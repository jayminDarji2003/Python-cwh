# Match case statements is similar to Switch case statements in other languages.
# In python we use MatchCase statements insted of switch statements.

# ex.

x = int(input("Enter any number between 0 to 10 : "))

match x:
    case 1:
        print("Entered value is 1")
    case 2:
        print("Entered value is 2")
    case 3:
        print("Entered value is 3")
    case 4:
        print("Entered value is 4")
    case 5:
        print("Entered value is 5")
    case 6:
        print("Entered value is 6")
    case 7:
        print("Entered value is 7")
    case 8:
        print("Entered value is 8")
    case 9:
        print("Entered value is 9")
    case 10:
        print("Entered value is 10")
    case _:
        print("You entered wrong value")
