fio = input("ФИО: ").split()
init = ''
kol = 0
for i in fio:
    init += i[0].upper()
    kol += len(i)
print(f"Инициалы: {init}.")
print(f"Длина (символов): {kol + len(init) - 1}")