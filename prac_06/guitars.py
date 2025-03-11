"""
Guitars
Estimate: 10 minutes
Actual:   20 minutes
"""
from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []
    guitar = get_guitar_info()
    while guitar is not None:
        guitars.append(guitar)
        display_guitar_info(guitar)
        guitar = get_guitar_info()
    display_total_guitars(guitars)


def get_guitar_info():
    """Get guitar info"""
    name = input("Name: ")
    if name == "":
        return None
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    return new_guitar


def display_guitar_info(guitar):
    """Display guitar info"""
    print(f"{guitar.name} ({guitar.year}): ${guitar.cost:.2f} added.\n")


def display_total_guitars(guitars):
    """Display total guitars"""
    print("There are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_string}")


main()