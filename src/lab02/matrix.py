from src.libraries.funcs import is_matrix_same

def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    This function transpose matrix
    
    Input data: list[float or int]
    Output data: list[list]
    Raises: ValueError('matrix has strings with different sizes'), TypeError('not a matrix')
    """

    if len(mat) == 0:
        return []
    if type(mat) != list:
        raise TypeError('not a matrix')

    if is_matrix_same(mat) != True: 
        raise ValueError('matrix has strings with different sizes')
    t = []
    for i in range(len(mat[0])):
        t.append([0] * len(mat))

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            t[j][i] = mat[i][j]
    return t

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    This function takes sums of strings
        
    Input data: list[float or int]
    Output data: list[float]
    Raises: ValueError('matrix has strings with different sizes'), TypeError('not a matrix')
    """
    if len(mat) == 0:
        return []
    if type(mat) != list:
        raise TypeError('not a matrix')
    if is_matrix_same(mat) != True: 
        raise ValueError('matrix has strings with different sizes')
    
    t = []
    for lst in mat:
        t.append(sum(lst))
    return t

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    This function takes sums of columns
        
    Input data: list[float or int]
    Output data: list[float]
    Raises: ValueError('matrix has strings with different sizes'), TypeError('not a matrix')
    """
    if len(mat) == 0:
        return []
    if type(mat) != list:
        raise TypeError('not a matrix')
    if is_matrix_same(mat) != True: 
        raise ValueError('matrix has strings with different sizes')
    
    t = [0] * (len(mat[0]))

    for lst in mat:
        for i in range(len(lst)):
            t[i] += lst[i]

    return t

#Tests
print(f'''
col_sums
[[1, 2, 3], [4, 5, 6]] → {col_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] → {col_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] → {col_sums([[0, 0], [0, 0]])}
[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}
''')