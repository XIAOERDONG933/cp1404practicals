import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    """Ask the user how many quick selections they want to generate."""
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        quick_pick = generate_picks()
        print(" ".join(f"{number:2}" for number in quick_pick))

def generate_picks():
    """Generate a list of numbers between the minimum and maximum values."""
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)

        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()

    return quick_pick

main()