"""
CP1404/CP5632 Practical
unreliable car
"""
from prac_09.car import Car
import random

class UnreliableCar(Car):
    """A car that might not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability chance."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven