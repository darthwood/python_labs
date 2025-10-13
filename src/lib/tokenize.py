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