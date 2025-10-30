"""CP1404/CP5632 Practical - Guitar class."""
"""
Guitar
Estimate: 15 minutes
Actual:   8 minutes
"""

CURRENT_YEAR = 2025

class Guitar:
    """Represent a Guitar object."""
    VINTAGE_AGE = 50

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Car Guitar."""
        self.name = name
        self.year = year
        self.cost = cost