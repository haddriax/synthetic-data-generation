import pandas as pd
import random


class PopulationSample:
    """
    Represents a sample of the generated synthetic population.
    Provides methods to augment the sample with additional characteristics.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        :param dataframe: DataFrame containing the generated data.
        """
        self.dataframe = dataframe
        # Store added characteristics and their generator details (for reference or re-generation)
        self.characteristics = {}

    def add_characteristic(self, name: str, characteristic):
        """
        Adds a new characteristic column to the sample.

        :param name: Name of the characteristic (i.e., the column name).
        :param characteristic: An instance of a characteristic generator that implements generate(n).

        :raise ValueError: The characteristic already exists when trying to insert it.
        """
        # @todo normalizing all columns names would be great (to lower)
        if name in self.dataframe.columns:
            raise ValueError(f"Trying to add {name} characteristic, but it already exists in the dataframe.")

        n = len(self.dataframe)
        generated_values = characteristic.generate(n)
        self.dataframe[name] = generated_values
        self.characteristics[name] = characteristic

    def get_sample(self) -> pd.DataFrame:
        """
        Returns the augmented DataFrame.
        """
        return self.dataframe
