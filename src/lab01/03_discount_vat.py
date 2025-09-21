price, discount, vat = map(int, input().split())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print('Вывод')
print(f'•База после скидки: {base:.2f} ₽')
print(f'•НДС: {vat_amount:.2f} ₽')
print(f'•Итого к оплате: {total:.2f} ₽')

# src/lab01/03_discount_vat.py
# 1000 10 20 
# Вывод
# •База после скидки: 900.00 ₽
# •НДС: 180.00 ₽
# •Итого к оплате: 1080.00 ₽