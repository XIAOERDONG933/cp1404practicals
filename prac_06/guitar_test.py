"""
Guitar Test
Estimate: 10 minutes
Actual:   15 minutes
"""

from guitar import Guitar
def main():
    """Test the logics of guitar class"""
    pass
    fender = Guitar("Fender", 2000, 16000)
    ibanez = Guitar("Ibanez", 1950, 1234.56)
    gibson = Guitar("Gibson L-5 CES", 1965, 23654.23)
    guitars = [fender, ibanez, gibson]
    expected_ages = [25, 75, 60]
    expected_is_vintage = [False, True, True]
    for guitar, expected_age in zip(guitars,expected_ages):
        print(f"{guitar.name} get_age() - Expected {expected_age}. "
              f"Got {guitar.get_age()}")

    for guitar, expected_age in zip(guitars,expected_is_vintage):
        print(f"{guitar.name} is_vintage() - Expected {expected_age}. "
              f"Got {guitar.is_vintage()}.")

main()