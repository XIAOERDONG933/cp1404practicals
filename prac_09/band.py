"""Band class for CP1404"""

class Band:
    """Band class that contains a collection of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musician_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_str})"

    def add(self, musician):
        """Add a musician to the band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of all musicians playing their instruments."""
        return "\n".join(musician.play() for musician in self.musicians)