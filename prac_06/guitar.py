"""
Guitar
Estimate: 10 minutes
Actual:   12 minutes
"""
CURRENT_YEAR = 2025

class Guitar:
    """Represents a guitar"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar"""
        return f"{self.name} {self.year} :  ${self.cost}"

    def get_age(self):
        """Returns how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if the guitar is 50 or more years"""
        return self.get_age() >= 50