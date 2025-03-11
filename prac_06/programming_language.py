"""
Programming Language
Estimate: 10 minutes
Actual:   32 minutes
"""
class ProgrammingLanguage:
    """Represents a programming language object"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if this programming language is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """String representation of the programming language"""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, "
                f"First appeared in {self.year}")