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

    def __str__(self):
        """Return the formatted string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the language has dynamic typing, otherwise False."""
        return self.typing.lower() == "dynamic"