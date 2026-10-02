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