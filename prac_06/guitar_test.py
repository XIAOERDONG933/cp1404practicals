"""CP1404/CP5632 Practical - The last two methods for testing guitars."""
"""
Guitar test
Estimate: 10 minutes
Actual:   13 minutes
"""

from prac_06.guitar import Guitar, CURRENT_YEAR

def main():
    """Demo test code to show how to use guitar class."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2020, 1000.00)

    # Test get_age()
    expected_age1 = CURRENT_YEAR - 1922
    expected_age2 = CURRENT_YEAR - 2020
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

    # Test is_vintage()
    expected_vintage1 = True
    expected_vintage2 = False
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {guitar2.is_vintage()}")

main()