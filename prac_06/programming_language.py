"""CP1404/CP5632 Practical - ProgrammingLanguage class."""
"""
Programming Languages
Estimate: 20 minutes
Actual:   10 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
