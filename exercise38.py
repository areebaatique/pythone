import random

best_score = None

while True:
    number = random.randint(1, 20)
    guesses = 0
    print("\nGuess the number between 1 and 20!")

    while True:
        try:
            guess = int(input("Your guess: "))
            guesses += 1
            if guess == number:
                print(f"Correct! You guessed it in {guesses} tries.")
                if best_score is None or guesses < best_score:
                    best_score = guesses
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        print(f"Best score: {best_score} guesses")
        break


