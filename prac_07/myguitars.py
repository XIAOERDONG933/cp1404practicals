"""
MyGuitars
Estimate: 16 minutes
Actual:   20 minutes
"""
from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Main function to read and show guitars"""
    guitars = read_data()
    guitars.sort()
    display_data(guitars)



def read_data():
    """Read data from guitars.csv"""
    guitars = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    return guitars


def display_data(guitars):
    """Display data from guitars"""
    for guitar in guitars:
        print(guitar)


main()