from pandas import read_json

from data.characteristics.characteristic import Characteristic
from utils.helpers import random_choice_proba


class GoalCharacteristic(Characteristic):
    def __init__(self):
        """
        :raise FileNotFoundError: If the file goals.json doesn't exist in the source folder.
        :raise KeyError: If the file goals.json doesn't have a single key named 'goals'.
        """
        json_path = 'source/goals.json'
        try:
            goals_df = read_json(json_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file containing the sport goals was not found.")

        try:
            self.goals_list = goals_df['goals'].dropna().tolist()
        except KeyError as e:
            raise KeyError(f"The key 'goals' does not exist in {json_path}.")

    def generate(self, n: int):
        return random_choice_proba(n, self.goals_list)
