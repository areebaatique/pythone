import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("Higher!")
    else:
        print("Lower!")
    guess = int(input("Guess again: "))

print("Correct! 🎉")

