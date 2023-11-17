# snake, water, gun exercise solution

import random


def check(user, comp):
    if user > 2 or user < 0:
        print("Invalid input")
        return "Retry"

    if comp == user:
        return 0

    if comp == 0 and user == 1:
        return -1

    if comp == 1 and user == 2:
        return -1

    if comp == 2 and user == 0:
        return -1

    return 1


while True:
    print("\n------- Choose any one --------")
    print("0 for Snake")
    print("1 for Water")
    print("2 for Gun")
    print("-1 for exit")
    user = int(input("Enter your choise : "))
    comp = random.randint(0, 2)

    if user == -1:
        break

    print(f"\nYou choose : {user}")
    print(f"Computer choose : {comp}")

    score = check(user, comp)

    if score == 0:
        print("It's a draw")
    elif score == 1:
        print("You won the game")
    elif score == -1:
        print("You loose the game")
    else:
        print(score)
