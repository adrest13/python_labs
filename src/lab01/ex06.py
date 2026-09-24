kol = int(input())

kol1 = kol2 = 0
for person in range(kol):
    opisanie = list(map(str, input().split()))
    if opisanie[3] == 'True':
        kol1 += 1
    elif opisanie[3] == 'False':
        kol2 += 1
print(kol1, kol2)