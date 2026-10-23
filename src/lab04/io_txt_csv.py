from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    This function reads text from the specified path
                
    Input data: path: str | Path, encoding: str = "utf-8"
    Output data: str
    '''

    return Path(path).read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    The function writes rows to a CSV file
                    
    Input data: rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
    Output data: None
    Raises: ValueError("Strings have the different sizes")
    '''
    
    p = Path(path)
    rows = list(rows)

    dlina = len(rows[0]);
    for row in rows:
        if len(row) != dlina:
            raise ValueError("Strings have different sizes")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    '''
    The function checks for the existence of the parent folder and creates it, along with any missing subfolders
                        
    Input data: rows: path: str | Path
    Output data: None
    '''

    Path(path).parent.mkdir(parents=True, exist_ok=True)
