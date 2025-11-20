"""
CP1404/CP5632 Practical
silver service taxi
"""
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A fancier version of Taxi with a flagfall charge."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the total fare including flagfall."""
        return super().get_fare() + self.flagfall