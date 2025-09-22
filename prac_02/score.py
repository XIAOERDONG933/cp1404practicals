"""This module implements a program that prompts users to enter scores and print the results,
and then generates random scores and prints their results."""

import random

def main():
    """Process user input, display results, and generate random scores."""
    score = float(input("Enter score: "))
    print(get_result(score))
    random_score = random.randint(0, 100)
    print(f"Your random score is {random_score}")
    print(get_result(random_score))

def get_result(score):
    """Determine the final grade based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

main()