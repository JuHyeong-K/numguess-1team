import random

answer = random.randint(1,100)
print(answer, type(answer))
chances = 5 # Try number

while chances > 0:
    user_guess = int(input("Guess the number: "))
    if answer == user_guess:
        chances -= 1
        print("CORRECT!")
    else:
        chances -= 1
        if chances == 0:
            print("WRONG! The correct number is {}.".format(answer))
            break
        print("Try again! You have {} chance(s)".format(chances))

