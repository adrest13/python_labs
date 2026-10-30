from pathlib import Path
import csv
from typing import Iterable, Sequence

def is_matrix_same(mat: list[list[float | int]]) -> bool:
    dlina = len(mat[0])
    for lst in mat:
        if len(lst) != dlina:
            return False
    return True

def ensure_parent_dir(path: str | Path) -> None:
    '''
    The function checks for the existence of the parent folder and creates it, along with any missing subfolders
                        
    Input data: rows: path: str | Path
    Output data: None
    '''

    Path(path).parent.mkdir(parents=True, exist_ok=True)