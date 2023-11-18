# Exercise : Library management system
# Question : create a library class with "no_of_books" and "books" as two instance variable. Write a program to create a library from this library class and show how you can print all books, add a books get the number of books using different methods. Show that your program doestn't persist the books after the program is stopped.

from Library import Library

l1 = Library(["Intro to programming", "Python", "Java", "DSA"])

student_name = input("Enter your name : ")

while True:
    print("\n\n--------- Welcome to the Library -------")
    print("1. Show Books")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Count the number of books")
    print("5. Exit")

    user_choice = int(input("\nEnter your choice : "))

    if user_choice == 1:
        print("\n")
        l1.get_books()

    elif user_choice == 2:
        print("\n")
        book_name = input("Enter book name : ")
        l1.add_book(book_name)

    elif user_choice == 3:
        print("\n")
        l1.remove_book()

    elif user_choice == 4:
        print("\n")
        l1.get_no_of_books()

    elif user_choice == 5:
        print("\n")
        print(f"Thank you {student_name}!!!")
        break

    else:
        print("Invalid input!!")
        print("Try again!!")
