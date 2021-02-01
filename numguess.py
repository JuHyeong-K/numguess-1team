import random

answer = random.randint(1,100)
user_guess = input("Guess the number: ")
print(user_guess)
print(answer, type(answer))

guess = 20
#TO DELETE UPON MERGE

if answer-guess==0:
    print("CORRECT!")
else:
    print("WRONG! The correct number is {}.".format(answer))
