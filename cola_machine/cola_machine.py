# Cola Machine
# Created by Josien Braas to practice Python


def provide_drink():
    """Provide the user with a selected beverage."""
    list_of_drinks = ["Coke", "Water", "Sprite", "Coffee", "Goat Milk"]
    print("\nHi there! Would you like a drink?\n")
    print("Choose one of the following: ")
    enum_drinks = list(enumerate(list_of_drinks, start=1))
    for drink in enum_drinks:
        print(str(drink[0]) + ". " + drink[1])
    try:
        choice = int(input("\nEnter the number of your preferred drink: "))
        if choice < 1 or choice > 5:
            print("\nError. choice was not valid, here is your money back.")
        else:
            drink = list_of_drinks[choice - 1]
            print("\n>> Here is your " + drink + "! <<")
    except ValueError:
        print("\nError. choice was not valid, here is your money back.")


if __name__ == "__main__":
    provide_drink()
