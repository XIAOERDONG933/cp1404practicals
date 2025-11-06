"""CP1404/CP5632 Practical - Guitar class."""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Car Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string in f-string format"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the current age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return true if the Guitar is in a vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year