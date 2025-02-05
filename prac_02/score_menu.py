import random

def get_valid_score():
    while True:
        try:
            score = float(input("Please enter a score between 0 and 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score, please ensure the score is between 0 and 100.")
        except ValueError:
            print("Invalid input, please enter a number.")


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_result(score):
    grade = determine_grade(score)
    print(f"Score: {score} → {grade}")

def show_stars(score):
    print("Stars: " + "*" * int(score))

def display_menu():
    print("\nMain Menu:")
    print("G - Get valid score")
    print("P - Print result")
    print("S - Show stars")
    print("Q - Quit")

def main():
    score = get_valid_score()

    choice = ""

    while choice != "Q":
        display_menu()  # Display the menu
        choice = input("Please enter your choice: ").upper()  # Get user choice and convert to uppercase

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using! Goodbye!")
        else:
            print("Invalid input, please choose again.")


if __name__ == "__main__":
    main()
