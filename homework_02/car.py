from homework_02.base import Vehicle
from homework_02.engine import Engine
from homework_02 import engine


class Car(Vehicle):
    engine = 3
    def __init__(self, weight, fuel, fuel_consumption):
        Vehicle().__init__()
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.engine = Engine


    def set_engine(self, engine):
        self.engine = engine
