"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
from homework_02 import engine

class Car(Vehicle):
    """
    в модуле car создайте класс Car
    класс Car должен быть наследником Vehicle
    добавьте атрибут engine классу Car
    """
    engine = 3
    def __init__(self, weight, fuel, fuel_consumption):
        Vehicle().__init__()
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.engine = Engine


    def set_engine(self, engine):
        """
        объявите метод set_engine, который принимает в себя
        экземпляр объекта Engine и устанавливает на текущий экземпляр Car
        """
        self.engine = engine
