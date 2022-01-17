"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    """
    создайте датакласс Engine в модуле engine,
    добавьте атрибуты volume и pistons
    """

    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons

