from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    @abstractmethod
    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @abstractmethod
    def increase_price(self):
        """Method increases the equipment’s price"""
        pass
