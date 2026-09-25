kol = int(input())

kol1 = kol2 = 0
for person in range(kol):
    opisanie = list(map(str, input(f"in_{person+1}: ").split()))
    if opisanie[3] == 'True':
        kol1 += 1
    elif opisanie[3] == 'False':
        kol2 += 1
print(f"out: {kol1} {kol2}")