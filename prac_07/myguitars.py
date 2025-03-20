"""
MyGuitars
Estimate: 16 minutes
Actual:   20 minutes
"""
from prac_06.guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Main function to read and show guitars"""
    guitars = read_data()
    guitar = get_guitar_info()
    while guitar is not None:
        guitars.append(guitar)
        guitar = get_guitar_info()
    # guitars.sort()
    display_data(guitars)
    save_guitars(guitars)



def read_data():
    """Read data from guitars.csv"""
    guitars = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


def display_data(guitars):
    """Display data from guitars"""
    for guitar in guitars:
        print(guitar)


def get_guitar_info():
    """Get guitar info"""
    name = input("Name: ")
    if name == "":
        return None
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    return new_guitar

def save_guitars(guitars):
    """Save guitar into the file"""
    out_file = open(FILENAME, "w")
    for guitar in guitars:
        out_file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}\n")
    out_file.close()



main()