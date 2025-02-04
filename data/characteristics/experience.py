from pandas import read_json

from data.characteristics.characteristic import Characteristic
from utils.helpers import random_choice_proba


class ExperienceCharacteristic(Characteristic):
    def __init__(self):
        """
        :raise FileNotFoundError: If the file experiences.json doesn't exist in the source folder.
        """
        # @todo Code a proper selection instead of just a random pull.
        # @todo Handle JSON format errors.
        try:
            experiences_df = read_json('source/experiences.json')
        except FileNotFoundError:
            raise FileNotFoundError(f"The file containing the experience levels was not found.")

        self.experiences_list = experiences_df['experiences'].dropna().tolist()

    def generate(self, n: int):
        return random_choice_proba(n, self.experiences_list, 1)
