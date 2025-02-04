from abc import ABC, abstractmethod


class Characteristic(ABC):
    @abstractmethod
    def generate(self, n: int):
        """
        Generate a list of values for this characteristic for n individuals.

        :param n: Number of samples.
        :return: A list (or other iterable) with n values.
        """
        pass
