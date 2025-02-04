import random


def injury_generator(n: int, muscles_list: list, injury_probability: float = 0.1):
    """
    Generates a list of injuries for n individuals. Each individual receives a random injury from
    the provided muscles_list with a chance given by injury_probability; otherwise, the value is None.

    :param n: Number of samples.
    :param muscles_list: List of muscle names (strings) that can be injured.
    :param injury_probability: Probability that an individual sustains an injury.
    :return: A list of injury labels or None.
    """
    return [
        random.choice(muscles_list) if random.random() < injury_probability else None
        for _ in range(n)
    ]
