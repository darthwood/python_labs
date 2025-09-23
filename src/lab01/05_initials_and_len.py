S = input()
M = S.strip()
M = M.replace('  ','')
k = len(M)
F = ''
for i in S:
    if i.isupper():
        F += i
print(f'Инициалы: {F}')
print(f'Длина (символов): {k}')

# src/lab01/05_initials_and_len.py
#       Иванов Иван Иванович
# Инициалы: ИИИ
# Длина (символов): 20