import pandas as pd
from pandas import read_csv

from data.characteristics.characteristic import Characteristic
from utils.helpers import random_choice_proba


class EquipmentCharacteristic(Characteristic):
    def __init__(self):
        """
        :raise FileNotFoundError: If the file equipements_row.csv doesn't exist in the source folder.
        :raise KeyError: If the file equipements_row.json doesn't have a single key named 'equipment_name'.
        """
        csv_path = 'source/equipments_rows.csv'
        try:
            equipments_df = read_csv(csv_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file containing the equipments was not found.")
        try:
            self.equipments_list = equipments_df['equipment_name'].dropna().tolist()
        except KeyError as e:
            raise KeyError(f"The key 'equipment_name' does not exist in {csv_path}.")

    def generate(self, n: int):
        l1 = random_choice_proba(n, self.equipments_list, 0.75)
        l2 = random_choice_proba(n, self.equipments_list, 0.30)
        l3 = random_choice_proba(n, self.equipments_list, 0.10)

        # Zip the lists and insert into a set to avoid duplicates. Only add an element if it's not None.
        # Always ensure we have at least "Aucun/poids du corps" in our set.
        return [{x for x in (elem1, elem2, elem3) if x is not None} | {"Aucun/poids du corps"}
                for elem1, elem2, elem3 in zip(l1, l2, l3)]
