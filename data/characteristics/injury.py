from pandas import read_json

from data.characteristics.characteristic import Characteristic
from utils.helpers import random_choice_proba


class InjuryCharacteristic(Characteristic):
    def __init__(self, injury_probability=0.1):
        """
        :param injury_probability: Probability that an individual sustains an injury.

        :raise FileNotFoundError: If the file muscles.json doesn't exist in the source folder.
        :raise KeyError: If the file muscles.json doesn't have a single key named 'muscles'.
        """
        json_path = 'source/muscles.json'
        try:
            muscles_df = read_json(json_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file containing the muscles that can be injured was not found.")

        try:
            self.muscles_list = muscles_df['muscles'].dropna().tolist()
        except KeyError as e:
            raise KeyError(f"The key 'muscles' does not exist in {json_path}.")
        self.injury_probability = injury_probability

    def generate(self, n: int):
        return random_choice_proba(n, self.muscles_list, self.injury_probability)
