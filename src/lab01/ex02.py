a = input("a: ")
b = input("b: ")

a = float(a.replace(',', '.'))
b = float(b.replace(',', '.'))

s = a + b
avg = s / 2

print(f"sum={s:.2f}; avg={avg:.2f}")