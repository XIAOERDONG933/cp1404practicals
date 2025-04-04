from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Represents an unreliable car."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drives the car by the given distance."""
        random_num = random.uniform(0, 100)
        if random_num < self.reliability:
            return super().drive(distance)
        return 0