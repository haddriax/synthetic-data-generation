from pandas import read_json

from data.characteristics.characteristic import Characteristic
from utils.helpers import random_choice_proba


class ExperienceCharacteristic(Characteristic):
    def __init__(self):
        """
        :raise FileNotFoundError: If the file experiences.json doesn't exist in the source folder.
        :raise KeyError: If the file experiences.json doesn't have a single key named 'experiences'.
        """
        # @todo Code a proper selection instead of just a random pull.
        json_path = 'source/experiences.json'
        try:
            experiences_df = read_json(json_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file containing the experience levels was not found.")
        try:
            self.experiences_list = experiences_df['experiences'].dropna().tolist()
        except KeyError as e:
            raise KeyError(f"The key 'experiences' does not exist in {json_path}.")

    def generate(self, n: int):
        return random_choice_proba(n, self.experiences_list, 1)
