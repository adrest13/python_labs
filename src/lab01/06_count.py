kol = int(input("in_1: "))

kol1 = kol2 = 0
for person in range(kol):
    opisanie = list(map(str, input(f"in_{person+2}: ").split()))
    if opisanie[3] == 'True':
        kol1 += 1
    elif opisanie[3] == 'False':
        kol2 += 1
print(f"out: {kol1} {kol2}")