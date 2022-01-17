from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    """
    доработайте базовый класс base.Vehicle:
    добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    добавьте инициализатор для установки weight, fuel, fuel_consumption
    """
    started: bool = False
    def __init__(self, weight: int = 8203, fuel: int = 5602, fuel_consumption: int = 10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        """
        добавьте метод start. При вызове этого метода необходимо проверить
        состояние started. И если не started, то нужно проверить,
        что топлива больше нуля, и обновить состояние started,
        иначе нужно выкинуть исключение exceptions.LowFuelError
        """
        if self.started == False:
            if self.fuel > 0:
                self.started = True
                return self.started
            else:
                raise LowFuelError


    def move(self, distance):
        """
        метод move, который проверяет, что топлива достаточно
        для преодоления переданной дистанции (вплоть до полного расхода),
        """
        self.fuel = self.fuel - distance * self.fuel_consumption

        if self.fuel >= 0:
            """
            и изменяет количество оставшегося топлива, иначе выкидывает
            исключение exceptions.NotEnoughFuel
            """
            self.fuel = self.fuel
        else:
            raise NotEnoughFuel


# vehicle = Vehicle()
# print("type vehicle.weight =", type(vehicle.weight) , vehicle.started, vehicle.fuel, vehicle.fuel_consumption, )
# print(vehicle.__dir__())
