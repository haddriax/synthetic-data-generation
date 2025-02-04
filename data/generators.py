import torch
import torch.distributions as dist
import pandas as pd
from data.models import BodyMeasurementDistributionData


class BodyMeasurementDistribution:
    """
    Generates synthetic body measurement data using a multivariate normal distribution.
    """

    def __init__(self, data: BodyMeasurementDistributionData):
        self.data = data
        self.group_name = data.group_name
        self.mean_height = data.mean_height
        self.std_height = data.std_height
        self.mean_weight = data.mean_weight
        self.std_weight = data.std_weight
        self.correlation_hw = data.correlation_hw
        self.mean_age = data.mean_age
        self.std_age = data.std_age
        self.num_samples = data.num_samples

        if not (-1 <= self.correlation_hw <= 1):
            raise ValueError("Correlation must be between -1 and 1.")
        if self.std_height < 0 or self.std_weight < 0:
            raise ValueError("Standard deviations must be non-negative.")
        if self.num_samples <= 0:
            raise ValueError("Number of samples must be positive.")

        self._distribution = self._create_body_distribution()

    def _create_body_distribution(self) -> dist.MultivariateNormal:
        mean_vector = torch.tensor([self.mean_height, self.mean_weight])
        cov_hw = self.correlation_hw * self.std_height * self.std_weight
        cov_matrix = torch.tensor([
            [self.std_height ** 2, cov_hw],
            [cov_hw, self.std_weight ** 2]
        ])
        return dist.MultivariateNormal(mean_vector, cov_matrix)

    def _create_age(self):
        samples = []
        while len(samples) < self.num_samples:
            needed = self.num_samples - len(samples)
            new_samples = torch.normal(self.mean_age, self.std_age, size=(needed * 2,))
            valid_samples = new_samples[(new_samples >= 18) & (new_samples <= 90)]
            samples.extend(valid_samples.tolist())
        return torch.tensor(samples[:self.num_samples], dtype=torch.int64)

    def sample_data(self) -> pd.DataFrame:
        """
        Generate a pandas DataFrame with columns: ['height', 'weight', 'group', 'age'].
        """
        samples = self._distribution.sample((self.num_samples,))
        age_samples = self._create_age()
        df = pd.DataFrame(samples.numpy(), columns=['height', 'weight'])
        df['group'] = self.group_name
        df['age'] = age_samples.numpy()

        df['height'] = pd.to_numeric(df['height'], errors='raise', downcast='float')
        df['weight'] = pd.to_numeric(df['weight'], errors='raise', downcast='float')
        df['group'] = df['group'].astype('string')
        return df

    def sample_numpy(self):
        """
        Returns the raw NumPy array of sampled data.
        """
        samples = self._distribution.sample((self.num_samples,))
        return samples.numpy()
