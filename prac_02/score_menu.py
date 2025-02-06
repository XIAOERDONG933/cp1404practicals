"""
Use menu to ask the user for a score and print the score status
and stars
"""
MENU = """G - Get a valid score (must be 0-100 inclusive)
P - Print result
S - Show stars
Q - Quit
"""

def main():
    print(MENU)
    # Get a valid score
    score = get_valid_score()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            print(score * "*")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


def get_valid_score():
    "Get a valid score"
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_score(score):
    """Determine score status"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()