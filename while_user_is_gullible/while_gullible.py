# While (user == gullible)
# Created by Josien Braas to practice Python


def ask_number():
    """Ask the user for a number."""
    counter = 0
    while True:
        number = input("\nHello! Please provide any number but " +
                       str(counter) + ": ")
        try:
            if int(number) == counter:
                print("Hey! You weren't supposed to enter " +
                      str(counter) + "!")
                break
        except ValueError:
            # print("Hey! That's not a number...")
            pass
        # if counter == 10:
        #     print("Wow, you're more patient than I am, you win.")
        #     break
        counter += 1

if __name__ == "__main__":
    ask_number()
