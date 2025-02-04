from pandas import read_json

from data.characteristics.characteristic import Characteristic
from utils.helpers import random_choice_proba


class InjuryCharacteristic(Characteristic):
    def __init__(self, injury_probability=0.1):
        """
        :param injury_probability: Probability that an individual sustains an injury.

        :raise FileNotFoundError: If the file muscles.json doesn't exist in the source folder.
        """

        # @todo Handle JSON format errors.
        try:
            muscles_df = read_json('source/muscles.json')
        except FileNotFoundError:
            raise FileNotFoundError(f"The file containing the muscles that can be injured was not found.")

        self.muscles_list = muscles_df['muscles'].dropna().tolist()
        self.injury_probability = injury_probability

    def generate(self, n: int):
        return random_choice_proba(n, self.muscles_list, self.injury_probability)
