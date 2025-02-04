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

    def add_characteristic(self, name: str, generator_function, **kwargs):
        """
        Adds a new characteristic column to the sample.

        :param name: Name of the characteristic (column name).
        :param generator_function: A callable that accepts an integer (number of samples) plus additional keyword
                                   arguments and returns an iterable of values of that length.
        :param kwargs: Keyword arguments to pass to the generator function.

        :raise ValueError: The characteristic already exists when trying to insert it.
        """
        # @todo normalize columns names
        if name in self.dataframe.columns:
            raise ValueError(f"Trying to add {name} characteristic, but it already exists in the dataframe.")

        n = len(self.dataframe)

        generated_values = generator_function(n, **kwargs)
        self.dataframe[name] = generated_values
        self.characteristics[name] = {
            'generator': generator_function,
            'params': kwargs
        }

    def get_sample(self) -> pd.DataFrame:
        """
        Returns the augmented DataFrame.
        """
        return self.dataframe
