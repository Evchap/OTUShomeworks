"""
Домашнее задание №2
Классы и модули
"""
"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    pass
# raise LowFuelError("MyException: LowFuelError")


class NotEnoughFuel(Exception):
    pass
# raise NotEnoughFuel('MyException: NotEnoughFuel')


class CargoOverload(Exception):
    pass
# raise CargoOverload('MyException: CargoOverload')


""" 
Важно: импортируйте модули и классы относительно корня проекта, 
а не папки с домашкой. 
То есть импорт исключений должен выглядеть 
так from homework_02.exceptions import LowFuelError, NotEnoughFuel 
или так from homework_02 import exceptions, 

(а не так from exceptions import LowFuelError, NotEnoughFuel, 
и не так import exceptions).
"""


