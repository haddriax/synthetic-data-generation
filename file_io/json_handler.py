import pandas as pd


def save_json(data: pd.DataFrame, file_path: str, human_readable: bool = False):

    if human_readable:
        json_lines = data.to_json(orient='records', lines=True, double_precision=3)
        records = json_lines.splitlines()
        # Add a tabulation for each record.
        records = ['\t' + record for record in records]
        # Add the '[]' that got removed using lines=True.
        with open(file_path, 'w') as f:
            f.write('[\n' + ',\n'.join(records) + '\n]')
    else:
        data.to_json(file_path, orient='records', lines=False, double_precision=3)
