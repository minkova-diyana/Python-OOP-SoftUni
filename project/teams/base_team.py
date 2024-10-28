from abc import ABC, abstractmethod
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    @abstractmethod
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage  # advantage in points that each team has
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []
        self.calculate_points()
        self.points = 0

    def calculate_points(self):
        self.points = self.advantage + sum([eq.protection for eq in self.equipment])

    def __eq__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            raise Exception('Game cannot start! Team types mismatch!')
        return self.points == other.points

    def __gt__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            raise Exception('Game cannot start! Team types mismatch!')
        return self.points > other.points

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Team name cannot be empty!')
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError('Team country should be at least 2 symbols long!')
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError('Advantage must be greater than zero!')
        self.__advantage = value

    @abstractmethod
    def win(self):
        """Increases the team’s advantage and the number of wins"""
        pass

    def get_statistics(self):
        total_equipment = sum([eq.price for eq in self.equipment])
        try:
            average_protection = int(sum([eq.protection for eq in self.equipment]) / len(self.equipment))
        except ZeroDivisionError:
            average_protection = 0

        return (f'Name: {self.name}\nCountry: {self.country}\n'
                f'Advantage: {self.advantage} points\n'
                f'Budget: {self.budget:.2f}EUR\n'
                f'Wins: {self.wins}\n'
                f'Total Equipment Price: {total_equipment:.2f}\n'
                f'Average Protection: {average_protection}')
