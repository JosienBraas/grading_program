# Bracketing Search
# Created by Josien Braas to practice Python

import random


def play_number_game_pick():
    number = random.randrange(1, 101)
    count_guesses = 1
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
                      ", and it only took you " + str(count_guesses) +
                      " tries! Congrats!\n")
                break
            count_guesses += 1
        except ValueError:
            print("That's not a number...\n")


def play_number_game_guess():
    print("\n>> Welcome to the number game! <<\n")
    print("Please pick a number between 1 and 100 and I will guess it.")
    choice = input("Ready? y/n: ")
    if choice.lower() == 'y':
        count_guesses = 1
        highest_number = 100
        lowest_number = 1
        number_guess = highest_number // 2
        while True:
            print("\nIs the number " + str(number_guess) + "?")
            answer = input("y(es) / h(igher) / l(ower): ")
            if answer.lower() == 'y':
                print("\nI guessed it in " + str(count_guesses) +
                      " tries! Yay me!")
                break
            elif answer.lower() == 'h':
                lowest_number = number_guess
                number_guess = (highest_number + number_guess) // 2
                count_guesses += 1
            elif answer.lower() == 'l':
                highest_number = number_guess
                number_guess = (lowest_number + number_guess) // 2
                count_guesses += 1
            else:
                print("I'm sorry, I didn't quite catch that.")
    else:
        print("\nOk, see you next time!\n")


if __name__ == "__main__":
    play_number_game_guess()
