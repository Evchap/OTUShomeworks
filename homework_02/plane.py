from homework_02.base import Vehicle
from homework_02 import exceptions



class Plane(Vehicle):
    cargo = 0
    max_cargo= 300

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo


    def load_cargo(self, new_cargo = 100):
        if self.max_cargo >= (self.cargo + new_cargo):
            self.cargo += new_cargo
        else:
            raise exceptions.CargoOverload


    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
