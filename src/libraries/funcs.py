def is_matrix_same(mat: list[list[float | int]]) -> bool:
    dlina = len(mat[0])
    for lst in mat:
        if len(lst) != dlina:
            return False
    return True