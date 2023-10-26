# Exercise 3 : Kaun Banega Crorepati
# Question : Create a program capable of displaying questions to the user like KBC.

# Initialize player's details
playerName = input("Enter your name: ")
playerMoney = 0

# Define questions, answer options, and correct answers
questions = [
    "What does the % operator do in Python?",
    "Which statement is used to exit a loop prematurely in Python?",
    "What is the result of 'Hello' + 'World' in Python?",
    "Which data structure in Python is an ordered collection of elements with no duplicate values?",
    "What does the len() function return for an empty list in Python?",
]

options = [
    ["A) Division", "B) Exponentiation", "C) Modulus (remainder)", "D) Multiplication"],
    ["A) continue", "B) return", "C) exit", "D) break"],
    ["A) 'HelloWorld'", "B) 'Hello World'", "C) 'Hello+World'", "D) Error"],
    ["A) List", "B) Tuple", "C) Set", "D) Dictionary"],
    ["A) 0", "B) 1", "C) 'Empty'", "D) None"],
]

correct_answers = ["C", "D", "A", "C", "A"]
money = [10000, 20000, 40000, 160000, 400000]

# Main game loop
for i in range(len(questions)):
    print("Q{}: {}".format(i + 1, questions[i]))
    for option in options[i]:
        print(option)

    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == correct_answers[i]:
        print("Correct answer!")
        playerMoney += money[i]
    else:
        print("Incorrect answer. The correct answer is", correct_answers[i])
        break  # End the game if the answer is incorrect

print(playerName, "Your total money is", playerMoney)
