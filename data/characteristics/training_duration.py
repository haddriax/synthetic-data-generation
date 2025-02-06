import torch
from data.characteristics.characteristic import Characteristic


class TrainingDurationCharacteristic(Characteristic):
    def __init__(self):
        """
        """
        pass

    def generate(self, n: int):
        """
        Generate a list of training durations (in minutes) for n individuals.
        The training duration is correlated with the individual’s experience level.

        :param n: Number of individuals.
        :return: List of training durations.
        """
        weights = torch.tensor([0.05, 0.08, 0.1], dtype=torch.float)

        cat_dist = torch.distributions.Categorical(probs=weights)

        samples = cat_dist.sample((n,))

        # /!\ Hardcoded way to have a step of 15. @todo change that ofc
        samples = (samples + 1) * 15
        return samples
