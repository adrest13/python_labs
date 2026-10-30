import json
import csv
from pathlib import Path
from src.lib.funcs import ensure_parent_dir


def json_to_csv(json_path: str, csv_path: str) -> None:
    '''
    The function reads data from JSON and writes it to a CSV (spreadsheet)
                    
    Input data: json_path: str, csv_path: str
    Output data: None
    Raises: FileNotFoundError("JSON file was not found"), ValueError("The file is not in JSON format"),
    ValueError("Empty file JSON"), ValueError("The JSON file is empty or has an invalid format")
    '''
    jp_file = Path(json_path)
    cp_file = Path(csv_path)

    if not jp_file.exists():
        raise FileNotFoundError("JSON file was not found")

    if jp_file.suffix.lower() != '.json':
        raise ValueError("The file is not in JSON format")

    try:
        with jp_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Not correct file JSON")

    if not isinstance(data, list) or not data:
        raise ValueError("The JSON file is empty or has an invalid format")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("All elements of a JSON list must be dictionaries.")

    fieldnames = []
    for element in data:
        for key in element:
            if key not in fieldnames:
                fieldnames.append(key)

    ensure_parent_dir(cp_file)

    with cp_file.open('w', newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for element in data:
            writer.writerow(element)


def csv_to_json(csv_path: str, json_path: str) -> None:
    '''
    The function reads data from JSON and writes it to a CSV (spreadsheet)
                        
    Input data: csv_path: str, json_path: str
    Output data: None
    Raises: FileNotFoundError("CSV file was not found"), ValueError("The file is not in CSV format"),
    ValueError("File CSV without fieldnames"), ValueError("File CSV is empty")
    '''
    jp_file = Path(json_path)
    cp_file = Path(csv_path)

    if not cp_file.exists():
        raise FileNotFoundError("CSV file was not found")

    if cp_file.suffix.lower() != '.csv':
        raise ValueError("The file is not in CSV format")

    with cp_file.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("File CSV without fieldnames")

        data = []
        for row in reader:
            data.append(row)

    if len(data) == 0:
        raise ValueError("File CSV is empty")

    ensure_parent_dir(jp_file)

    with jp_file.open('w', encoding='utf-8') as p:
        json.dump(data, p, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    json_to_csv(r'data\lab05\samples\people.json', r'data\lab05\out\people_from_json.csv')
    csv_to_json(r'data\lab05\samples\cities.csv', r'data\lab05\out\people_from_csv.json')
