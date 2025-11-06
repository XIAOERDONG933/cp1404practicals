"""
CP1404/CP5632 Practical
My Guitars
"""
from prac_07.guitar import Guitar, CURRENT_YEAR

FILENAME = "guitars.csv"

def main():
    """Main program to manage guitar collection."""
    guitars = load_guitars(FILENAME)

    print("\nOriginal guitar list:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)

    print("\nEnter new guitars (blank name to finish)")
    guitars = add_guitars_recursively(guitars)

    save_guitars(FILENAME, guitars)

    print("\nFinal guitar list:")
    guitars.sort()
    display_guitars(guitars)