# Grading Program
# Created by Josien Braas to practice Python

import random


def check_grade():
    """Ask the user for a grade score input and give feedback."""
    list_of_classes = ['"The Wonders of Java"',
                       '"Python for President"',
                       '"Stay Sharp with C#"',
                       '"OMG Lisp!"',
                       '"Some CSS a day keeps the doctor away"']

    print("\nHi there, you have finished the course " +
          random.choice(list_of_classes) +
          ". Congratulations!")

    try:
        grade = int(input("\nWhat was your score? "))
        give_feedback(grade)
    except ValueError:
        print("That is not a valid number.")


def give_feedback(grade):
    """Provide fitting feedback on a given grade score."""
    feedback_dictionary = {0: "That is not a valid score.",
                           1: "Perfect score!",
                           2: "You scored an A!",
                           3: "You scored a B!",
                           4: "You scored a C!",
                           5: "You scored a D!",
                           6: "You scored an F!"}

    key = 0

    if grade == 100:
        key = 1
    elif 90 <= grade < 100:
        key = 2
    elif 80 <= grade < 90:
        key = 3
    elif 70 <= grade < 80:
        key = 4
    elif 60 <= grade < 70:
        key = 5
    elif 0 <= grade < 60:
        key = 6

    print(feedback_dictionary[key])


if __name__ == "__main__":
    check_grade()
