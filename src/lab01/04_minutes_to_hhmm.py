m = int(input('Минуты:'))
h = m // 60
mi = m%60
print(f'{h}:{str(mi).zfill(2)}')

# src/lab01/04_minutes_to_hhmm.py
# Минуты:135
# 2:15