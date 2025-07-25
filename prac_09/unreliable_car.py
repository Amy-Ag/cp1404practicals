import random

from car import Car

class UnreliableCar(Car):
    """Unreliable version of car to make it not drive."""
    def __init__(self,name,fuel,reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self,distance):
        """Drive car only if random number is less than car's reliability."""
        if random.uniform(0,100) < self.reliability:
            return super().drive(distance)
        else:
            return 0