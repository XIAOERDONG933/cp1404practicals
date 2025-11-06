"""CP1404/CP5632 Practical - Store all users' guitars and print them."""
"""
Guitars
Estimate: 20 minutes
Actual:   21 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Get and display guitars."""
    guitars = get_guitars()

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    display_guitars(guitars)

def get_guitars():
    """Get a list of guitars from user input."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    return guitars


def display_guitars(guitars):
    """Display the list of guitars."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()