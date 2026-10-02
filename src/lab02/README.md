## ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

### Задание 1 (arrays.py)
Программа находит минимум и максимум. Затем выводит кортеж из этих 2 значений
```py
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    This function takes list and returns pair (min, max)

    Input data: list[float or int]
    Output data: tuple(float or int)
    Raises: ValueError(list is empty), TypeError('not a matrix')
    """

    if len(nums) == 0:
        raise ValueError("list is empty")
    if type(nums) != list and type(nums) != tuple:
        raise TypeError ('not a matrix')
    mn = 1000000500000000
    mx = -1000000000005000000
    for i in nums:
        if mn > i:
            mn = i
        if mx < i:
            mx = i
    return (mn, mx)

#Tests
print(f'''
min_max
[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}
[42] -> {min_max([42])}
[-5, -2, -9] -> {min_max([-5, -2, -9])}
[] -> {min_max([])} 
[1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}
''')
```

![](../../images/lab02/min_max.png)<br>
*Результат выполнения функции min_max()*

### Задание 2 (arrays.py)
На вход подается список. Выводим отсортированный список без повторяющихся элементов
```py
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    This function sorts elements
    
    Input data: list[float or int]
    Output data: list[float or int]
    Raises: TypeError('not a matrix')
    """

    if type(nums) != list:
        raise TypeError ('not a matrix')

    nums = list(set(nums))
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
    

#Tests
print(f'''
unique_sorted
[3, 1, 2, 1, 3] -> {unique_sorted([3, 1, 2, 1, 3])}
[] -> {unique_sorted([])}
[-1, -1, 0, 2, 2] -> {unique_sorted([-1, -1, 0, 2, 2])}
[1.0, 1, 2.5, 2.5, 0] -> {unique_sorted([1.0, 1, 2.5, 2.5, 0])}
''')
```

![](../../images/lab02/unique_sorted.png)<br>
*Результат выполнения функции unique_sorted()*

### Задание 3 (arrays.py)
Программа расщепляет список из списков или кортежей в один список
```py
def flatten(mat: list[list | tuple]) -> list[float | int]:
    """
    This function changes list with lists or tuples in one big list
        
    Input data: list[list or tuple]
    Output data: list[float or int]
    Raises: TypeError('not a matrix and not a tuple'), TypeError('not float and not int in list[list or tuple]')
    """

    answer = []
    for lst in mat:
        if type(lst) != list and type(lst) != tuple:
            raise TypeError ('not a matrix and not a tuple')
        for element in lst:
            answer.append(element)
    return answer


#Tests
print(f'''
flatten
[[1, 2], [3, 4]] -> {flatten([[1, 2], [3, 4]])}
[[1, 2], (3, 4, 5)] -> {flatten([[1, 2], (3, 4, 5)])}
[[1], [], [2, 3]] -> {flatten([[1], [], [2, 3]])}
[[1, 2], "ab"] -> {flatten([[1, 2], "ab"])}
''')
```

![](../../images/lab02/flatten.png)<br>
*Результат выполнения функции flatten()*

### Задание 4 (matrix.py)
Подается матрица из матриц. В выходных данных получаем транспонированную матрицу
```py
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

#Tests
print(f'''
transpose
[[1, 2, 3]] -> {transpose([[1, 2, 3]])}
[[1], [2], [3]] -> {transpose([[1], [2], [3]])}
[[1, 2], [3, 4]] -> {transpose([[1, 2], [3, 4]])}
[] -> {transpose([])}
[[1, 2], [3]] -> {transpose([[1, 2], [3]])}
''')
```

![](../../images/lab02/transpose.png)<br>
*Результат выполнения transpose()*

### Задание 5 (matrix.py)
На вход подается список. Выводим сумму в каждой строке списка
```py
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

#Tests
print(f'''
row_sums
[[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}
[[1, 2], [3]] -> {row_sums([[1, 2], [3]])}
''')
```

![](../../images/lab02/row_sums.png)<br>
*Результат выполнения функции row_sums()*

### Задание 6 (matrix.py)
На вход подается список. Выводим сумму в каждом столбце списка
```py
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
```

![](../../images/lab02/col_sums.png)<br>
*Результат выполнения функции col_sums()*

### Задание 7 (tuples.py)
Работа с кортежами (fio, group, gpa)
```py
def format_record(rec: tuple[str, str, float]) -> str:
    """
    We need to work with tuple
        
    Input data: tuple[str, str, float]
    Output data: str
    Raises: TypeError('not a tuple')
    TypeError('fio must be string')
    TypeError('gpa must be int or float')

    ValueError('we need 3 elements in tuple')
    ValueError('you need to enter full fio')
    ValueError('grop can\'t be empty')
    ValueError('we need 0 <= gpa <= 50')
    """

    if type(rec) != tuple:
        raise TypeError('not a tuple')
    if type(rec[0]) != str:
        raise TypeError('fio must be string')
    if type(rec[0]) != str:
            raise TypeError('group must be string')
    if (type(rec[2]) != float) and (type(rec[2]) != int):
        raise TypeError('gpa must be int or float')
    
    if len(rec) != 3:
        raise ValueError('we need 3 elements in tuple')
    if len(rec[0].strip().split()) != 3 and len(rec[0].strip().split()) != 2:
        raise ValueError('you need to enter full fio')
    if len(rec[1].strip()) == 0:
        raise ValueError('grop can\'t be empty')
    if (rec[2] < 0) or (rec[2] > 50):
        raise ValueError('we need 0 <= gpa <= 50')

    string = rec[0].strip().split()
    fio = ""
    flag = 0
    for i in range(len(string)):
        if flag == 0:
            fio += string[i][0].upper() + string[i][1:] + " "
            flag = 1
        else:
            fio += string[i][0].upper() + "."
    
    return f"{fio}, гр. {rec[1].strip()}, GPA {rec[2]:.2f}"

#Tests
print(f'''
("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}
''')
```

![](../../images/lab02/tuples.png)<br>
*Результат выполнения tuples()*