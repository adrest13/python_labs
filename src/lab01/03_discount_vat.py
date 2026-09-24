price = float(input("price="))
discount = float(input("discount="))
vat = float(input("vat="))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽", f"НДС:               {vat_amount:.2f} ₽", f"Итого к оплате:    {total:.2f} ₽", sep = "\n")