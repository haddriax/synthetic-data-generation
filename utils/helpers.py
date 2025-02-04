import random


def random_choice_proba(n: int, source_list: list, probability: float = 1.0):
    """
    Generates a list of size n. Each individual receives a random injury from
    the provided muscles_list with a chance given by injury_probability; otherwise, the value is None.

    :param n: Number of samples.
    :param source_list: List where the choice will be pulled from.
    :param probability: Probability to pull something from the source_list.
    :return: A list of source_list items or None.
    """
    return [
        random.choice(source_list) if random.random() < probability else None
        for _ in range(n)
    ]