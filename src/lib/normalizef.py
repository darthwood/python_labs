def normalize(n):
    import re
    n = n.casefold().strip()
    s = re.sub(r'[^ёa-zA-Zа-яА-Я,-]', ' ', n)
    s = s.replace('ё', 'е')
    s = s.split()
    s = ' '.join(s)
    return s