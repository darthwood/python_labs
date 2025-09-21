N = int(input())
O = 0
Z = 0
for i in range(N):
    inpup = list(input().split(' '))
    if 'True' in inpup:
        O += 1
    else:
        Z += 1
print(O, Z)

# src/lab01/06_schet_stud.py
# 3
# Максимов Максим 18 True
# Геннадьев Геннадий 17 False
# Алексеев Алексей 17 True
# 2 1