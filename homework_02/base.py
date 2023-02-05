from abc import ABC
import homework_02.exceptions as exceptions


class Vehicle(ABC):
    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 0, started: bool = False):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: float):
        remainder = self.fuel - self.fuel_consumption * distance
        if remainder >= 0:
            self.fuel = remainder
        else:
            raise exceptions.NotEnoughFuel("Not Enough Fuel")