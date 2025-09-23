S = input()
M = S.strip().split()
L = ' '.join(M)
k = len(L)
F = ''
for i in M:
    F += i[0]
print(L)
print(f'Инициалы: {F}')
print(f'Длина (символов): {k}')

# src/lab01/05_initials_and_len.py
#    Иванов   Иван   Иванович
# Иванов Иван Иванович
# Инициалы: ИИИ
# Длина (символов): 20