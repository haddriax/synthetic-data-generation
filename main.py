import multiprocessing
import pandas as pd

from data.characteristics.goal import GoalCharacteristic
from data.models import BodyMeasurementDistributionData
from data.generators import BodyMeasurementDistribution
from file_io.json_handler import save_json
from plotting.plots import DistributionVisualizer, Graph
from config import OUTPUT_JSON


def worker(distribution_settings: BodyMeasurementDistributionData):
    generator = BodyMeasurementDistribution(distribution_settings)
    return generator.sample_data()


def main(distributions_data: list[BodyMeasurementDistributionData], plot_type: Graph = Graph.NO_GRAPH):
    with multiprocessing.Pool(processes=len(distributions_data)) as pool:
        dataframes = pool.map(worker, distributions_data)

    if plot_type != Graph.NO_GRAPH:
        DistributionVisualizer.plot_distributions(dataframes=dataframes, graph_type=plot_type)

    # Wrap the generated data in a PopulationSample.
    from data.population_sample import PopulationSample
    concat_dataframes = pd.concat(dataframes)

    sample = PopulationSample(concat_dataframes)

    # Generate more data by inserting characteristics.
    from data.characteristics.injury import InjuryCharacteristic
    try:
        injury_char = InjuryCharacteristic(injury_probability=0.10)
        sample.add_characteristic('injury', injury_char)
    except FileNotFoundError as e:
        print(f" InjuryCharacteristic has been skipped: \n reason: {e}")
    except KeyError as e:
        print(f" InjuryCharacteristic has been skipped: \n reason: {e}")

    from data.characteristics.experience import ExperienceCharacteristic
    try:
        experience_char = ExperienceCharacteristic()
        sample.add_characteristic('experience_level', experience_char)
    except FileNotFoundError as e:
        print(f" ExperienceCharacteristic has been skipped: \n reason: {e}")
    except KeyError as e:
        print(f" ExperienceCharacteristic has been skipped: \n reason: {e}")

    try:
        experience_char = GoalCharacteristic()
        sample.add_characteristic('main_goal', experience_char)
    except FileNotFoundError as e:
        print(f" GoalCharacteristic has been skipped: \n reason: {e}")
    except KeyError as e:
        print(f" GoalCharacteristic has been skipped: \n reason: {e}")

    from data.characteristics.training_duration import TrainingDurationCharacteristic
    training_duration_char = TrainingDurationCharacteristic()
    sample.add_characteristic('training_duration', training_duration_char)
    try:
        from data.characteristics.equipment import EquipmentCharacteristic
        equipment_char = EquipmentCharacteristic()
        sample.add_characteristic('equipment', equipment_char)
    except FileNotFoundError as e:
        print(f" EquipmentCharacteristic has been skipped: \n reason: {e}")
    except KeyError as e:
        print(f" EquipmentCharacteristic has been skipped: \n reason: {e}")

    save_json(sample.get_sample(), OUTPUT_JSON, True)


if __name__ == "__main__":
    body_distributions_data = [
        BodyMeasurementDistributionData(
            group_name="Men",
            mean_height=178.0,
            mean_weight=80.0,
            std_height=6.0,
            std_weight=8.0,
            correlation_hw=0.60,
            mean_age=36,
            std_age=8,
            samples=50
        ),
        BodyMeasurementDistributionData(
            group_name="Women",
            mean_height=165.0,
            mean_weight=65.0,
            std_height=6.0,
            std_weight=9.0,
            correlation_hw=0.45,
            mean_age=36,
            std_age=8,
            samples=50
        )
    ]

    main(body_distributions_data, Graph.NO_GRAPH)
