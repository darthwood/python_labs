from umbapumpa import *
import sys

s = sys.stdin.readline()
e = normalize(s)
t = tokenize(e)
c = sorted(count_freq(t).items(),key=lambda item: item[1], reverse=True)[:5]

kol = len(t)
spis = len(set(t))

print(f'Всего слов: {kol}')
print(f'Уникальных слов: {spis}')
print('Топ-5:')
for i in c:
    print(normalize(str(i)).replace(',',':').replace(' ',''))

# src/lab03/stdin.py
# "Привет, мир! Привет!!!"
# Всего слов: 3
# Уникальных слов: 2
# Топ-5:
# привет:2
# мир:1    