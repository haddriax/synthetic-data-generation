import pandas as pd


def save_json(data: pd.DataFrame, file_path: str):
    data.to_json(file_path, orient='records')
