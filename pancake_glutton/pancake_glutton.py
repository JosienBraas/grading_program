# Pancake Glutton
# Created by Josien Braas to practice Python


def get_pancake_stats():
    """Ask the user for the pancake numbers."""
    print("\nPlease provide the pancake intake for our visitors:\n")
    list_of_people = []
    for i in range(1, 11):
        first_item = "Person " + str(i)
        second_item = input(first_item + ": ")
        try:
            new_tuple = first_item, int(second_item)
        except ValueError:
            new_tuple = first_item, 0
        list_of_people.append(new_tuple)
    sorted_list_of_people = sort_pancake_list(list_of_people)
    print("\nThe person who ate the most pancakes is " +
          sorted_list_of_people[0][0] + " with " +
          str(sorted_list_of_people[0][1]) + " pancakes.")
    print("\nThe person who ate the least pancakes is " +
          sorted_list_of_people[9][0] + " with " +
          str(sorted_list_of_people[9][1]) + " pancakes.")
    print("\nOrder of pancakes eaten:")
    for j in sorted_list_of_people:
        print(j[0] + ": ate " + str(j[1]) + " pancakes")


def sort_pancake_list(list_of_people):
    """Return sorted list (high to low) of pancake eaters."""
    sorted_list_of_people = []
    for f in sorted(list_of_people, key=lambda bl: bl[1], reverse=True):
        sorted_list_of_people.append(f)
    return sorted_list_of_people


if __name__ == "__main__":
    get_pancake_stats()
