# While (user == gullible)
# Created by Josien Braas to practice Python


def ask_number():
    """Ask the user for a number."""
    while True:
        number = input("\nHello! Please provide any number but 5: ")
        try:
            if int(number) == 5:
                print("Hey! You weren't supposed to enter 5!")
                break
        except ValueError:
            print("Hey! That's not a number!")

if __name__ == "__main__":
    ask_number()
