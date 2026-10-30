import csv
from pathlib import Path
from openpyxl import Workbook
from src.lib.funcs import ensure_parent_dir


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    '''
    The function writes data from CSV into XSLX

    Input data: csv_path: str, xlsx_path: str
    Output data: None
    Raises: FileNotFoundError("CSV file was not found"), ValueError("The file is not in CSV format"),
    ValueError("File CSV is empty")
    '''
    cp_file = Path(csv_path)
    xlp_file = Path(xlsx_path)

    if not cp_file.exists():
        raise FileNotFoundError("CSV file was not found")

    if cp_file.suffix.lower() != '.csv':
        raise ValueError("The file is not in CSV format")

    with cp_file.open('r', newline='', encoding='utf-8') as f:
        reader = []
        for row in csv.reader(f):
            reader.append(row)

    if len(reader) == 0:
        raise ValueError("File CSV is empty")

    wb = Workbook()
    w = wb.active
    assert w is not None
    w.title = "List"

    for row in reader:
        w.append(row)

    for col in w.columns:
        letter = col[0].column_letter
        max_len = 0

        for cell in col:
            if cell.value:
                cell_len = len(str(cell.value))
                max_len = max(max_len, cell_len)

        if max_len < 8:
            max_len = 8

        w.column_dimensions[letter].width = max_len

    ensure_parent_dir(xlp_file)
    wb.save(xlp_file)


if __name__ == '__main__':
    csv_to_xlsx(r"data/lab05/samples/people.csv", r"data/lab05/out/people.xlsx")
