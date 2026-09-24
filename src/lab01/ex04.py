minutes = int(input("Минуты: "))

hours = minutes // 60
minutes -= 60 * hours
hours %= 24

print(f"{hours}:{minutes:02d}")