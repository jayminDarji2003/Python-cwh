# custom error : raise keyword

num = int(input("Enter a number between 5 and 9 : "))

if(num<5 or num>9):
    raise ValueError("Invalid number")
