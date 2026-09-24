string = input()

for i in range(len(string)):
    if 0 <= (ord(string[i]) - 65) <= 25:
        up_char = string[i]
        num = i
        break

final = up_char
for i in range(num, len(string)):
    if 48 <= ord(string[i]) <= 57:
        final += string[i + 1]
        step = i + 1 - num
        num = i + 1
        break

while num + step < len(string):
    num += step
    final += string[num]
    if string[num] == '.':
        break
print(final)