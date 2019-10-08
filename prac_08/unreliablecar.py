from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random = randint(1, 100)
        if random >= self.reliability:
            distance = 0
        actual_drive = super().drive(distance)
        return actual_drive
