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
print('________________________________')
m_len = 5
for a, b in c:
    m_len = max(m_len, len(a))
print(f'Слово{" "*(m_len-4)}| Частота')
print('________________________________')
for x,y in c:
    print(f'{x}{" "* (m_len - len(x)+1)}| {y}')


# "Привет, мир! Привет!!!"
# Всего слов: 3
# Уникальных слов: 2
# Топ-5:
# ________________________________
# Слово  | Частота
# ________________________________
# привет | 2
# мир    | 1