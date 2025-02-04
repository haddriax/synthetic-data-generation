class BodyMeasurementDistributionData:
    def __init__(
            self,
            group_name: str,
            mean_height: float,
            std_height: float,
            mean_weight: float,
            std_weight: float,
            correlation_hw: float,
            mean_age: int,
            std_age: int,
            samples: int
    ):
        """
        :param group_name:       Label for the distribution (e.g. "Men", "Women")
        :param mean_height:      Mean of the height distribution
        :param std_height:       Standard deviation of height
        :param mean_weight:      Mean of the weight distribution
        :param std_weight:       Standard deviation of weight
        :param correlation_hw:   Correlation between height and weight (between -1 and 1)
        :param mean_age:         Mean age
        :param std_age:          Standard deviation of age
        :param samples:          Number of samples to generate
        """
        self.group_name = group_name
        self.mean_height = mean_height
        self.std_height = std_height
        self.mean_weight = mean_weight
        self.std_weight = std_weight
        self.correlation_hw = correlation_hw
        self.mean_age = mean_age
        self.std_age = std_age
        self.num_samples = samples
