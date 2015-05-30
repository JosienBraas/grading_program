# Bracketing Search
# Created by Josien Braas to practice Python

import random


def play_number_game():
    number = random.randrange(1, 101)
    print("\n>> Welcome to the number game! <<\n")
    while True:
        guess = input("Please guess the number: ")
        try:
            if int(guess) > number:
                print("Too high!\n")
            elif int(guess) < number:
                print("Too low!\n")
            else:
                print("\nYou guessed the number, " + str(number) +
                      "! Congrats!\n")
                break
        except ValueError:
            print("That's not a number...\n")

if __name__ == "__main__":
    play_number_game()
