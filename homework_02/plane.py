from homework_02.base import Vehicle
from homework_02 import exceptions



class Plane(Vehicle):
    """
    создайте класс `Plane`, наследник `Vehicle`
    в модуле plane создайте класс Plane
    класс Plane должен быть наследником Vehicle
    """

    cargo = 0
    max_cargo= 300

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo


    def load_cargo(self, new_cargo = 100):
        """
        объявите метод load_cargo, который принимает число, проверяет,
        что в сумме с текущим cargo не будет перегруза, и обновляет
        значение, в ином случае выкидывает исключение exceptions.CargoOverload
        """
        if self.max_cargo >= (self.cargo + new_cargo):
            self.cargo += new_cargo
        else:
            raise exceptions.CargoOverload


    def remove_all_cargo(self):
        """
        объявите метод remove_all_cargo, который обнуляет значение cargo и
        возвращает значение cargo, которое было до обнуления
        """
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
