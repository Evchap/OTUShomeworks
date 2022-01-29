from homework_02.base import Vehicle


class Car(Vehicle):
    engine = 3
    def __init__(self, weight, fuel, fuel_consumption):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)


    def set_engine(self, engine):
        self.engine = engine
