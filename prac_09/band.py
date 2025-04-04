class Band:
    """Represents a band"""
    def __init__(self,name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Adds a musician to the band"""
        self.musicians.append(musician)

    def play(self):
        """Plays the band"""
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        """String representation of the band"""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"