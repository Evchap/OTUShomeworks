from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    started: bool = False
    def __init__(self, weight: int = 8203, fuel: int = 5602, fuel_consumption: int = 10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
                return self.started
            else:
                raise LowFuelError


    def move(self, distance):
        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel