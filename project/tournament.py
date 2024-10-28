from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_TYPES = {'KneePad': KneePad, 'ElbowPad': ElbowPad, 'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # The number of teams а Tournament can have
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError('Tournament name should contain letters and digits only!')
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_TYPES:
            raise Exception('Invalid equipment type!')
        equipment = self.VALID_TYPES[equipment_type]()
        self.equipment.append(equipment)
        return f'{equipment_type} was successfully added.'

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TYPES:
            raise Exception('Invalid team type!')
        if self.capacity <= len(self.teams):
            return 'Not enough tournament capacity.'
        team = self.VALID_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f'{team_type} was successfully added.'

    def get_team_name(self, name):
        return [t for t in self.teams if t.name == name][0]

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.get_team_name(team_name)
        equipment = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type][-1]
        if team.budget < equipment.price:
            raise Exception('Budget is not enough!')
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f'Successfully sold {equipment_type} to {team_name}.'

    def remove_team(self, team_name: str):
        try:
            team = self.get_team_name(team_name)
        except IndexError:
            raise Exception('No such team!')
        if team.wins > 0:
            raise Exception(f'The team has {team.wins} wins! Removal is impossible!')
        self.teams.remove(team)
        return f'Successfully removed {team_name}.'

    def increase_equipment_price(self, equipment_type: str):
        counter = 0
        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                counter += 1
        return f'Successfully changed {counter}pcs of equipment.'

    def play(self, team_name1: str, team_name2: str):
        team_1 = self.get_team_name(team_name1)
        team_2 = self.get_team_name(team_name2)
        team_1.calculate_points()
        team_2.calculate_points()
        if team_1 == team_2:
            return 'No winner in this game.'
        team_1.win() if team_1 > team_2 else team_2.win()
        return f'The winner is {team_1.name if team_1 > team_2 else team_2.name}.'

    def get_statistics(self):
        result = f'Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n'
        result += '\n'.join(t.get_statistics() for t in self.teams)
        return result
