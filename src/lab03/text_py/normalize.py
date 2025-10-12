n1 = "ПрИвЕт\nМИр\t"
n2 = "ёжик, Ёлка"
n3 = "Hello\r\nWorld"
n4 = "  двойные   пробелы  "

def normalize(n):
    import re
    n = n.casefold().strip()
    s = re.sub(r'[^ёa-zA-Zа-яА-Я,-]', ' ', n)
    s = s.replace('ё', 'е')
    s = s.split()
    s = ' '.join(s)
    return s

print(normalize(n1))
print(normalize(n2))
print(normalize(n3))
print(normalize(n4))

# src/lab03/text_py/normalize.py
# привет мир
# ежик, елка
# hello world
# двойные пробелы