t1 = "привет мир" #→ ["привет", "мир"]
t2 = "hello,world!!!" #→ ["hello", "world"]
t3 = "по-настоящему круто" #→ ["по-настоящему", "круто"]
t4 = "2025 год" #→ ["2025", "год"]
t5 = "emoji 😀 не слово" #→ ["emoji", "не", "слово"] (эмодзи выпадают)


def normalize1(n):
    import re
    n = n.casefold().strip()
    s = re.sub(r'[^0-9ёa-zA-Zа-яА-Я-]', ' ', n)
    s = s.replace('ё', 'е')
    s = s.split()
    s = ' '.join(s)
    return s

def tokenize(n):
    s = normalize1(n)
    return s.split(' ')

print(tokenize(t1))
print(tokenize(t2))
print(tokenize(t3))
print(tokenize(t4))
print(tokenize(t5))

# ['привет', 'мир']
# ['hello', 'world']
# ['по-настоящему', 'круто']
# ['год']
# ['emoji', 'не', 'слово']