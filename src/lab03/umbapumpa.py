def unique_sorted(n):
    n = set(n)
    m = list()
    for i in n:
        try:
            if int(i) == float(i):
                m.append(int(i))
        except:
            try:
                m.append(float(i))
            except:
                return '[]'
    return sorted(set(m))

def transpose(n):
    s = []
    for i in range(len(n)-1):
        if len(n[i]) != len(n[i+1]):
            return 'ValueError'
    if n == []:
        return []
    cls = len(n)
    rws = len(n[0])
    for x in range(rws):
        res = []
        for y in range(cls):
            res.append(n[y][x])
        s.append(res)
    return s

def tokenize(n):
    import re
    n = n.casefold().strip()
    s = re.sub(r'[^0-9ёa-zA-Zа-яА-Я-]', ' ', n)
    s = s.replace('ё', 'е')
    s = s.split()
    s = ' '.join(s)
    return s.split(' ')

def normalize(n):
    import re
    n = n.casefold().strip()
    s = re.sub(r'[^0-9ёa-zA-Zа-яА-Я,-]', ' ', n)
    s = s.replace('ё', 'е')
    s = s.split()
    s = ' '.join(s)
    return s

def row_sums(n):
    s = []
    for i in range(len(n)-1):
        if len(n[i]) == len(n[i+1]):
            s.append(sum(n[i]))
        else:
            return 'ValueError'
    s.append(sum(n[i]))
    return s

def min_max(n):
    n = set(n)
    m = list()
    for i in n:
        try:
            if int(i) == float(i):
                m.append(int(i))
        except:
            try:
                m.append(float(i))
            except:
                return 'ValueError'
    return min(m),max(m)

def format_record(n):
    fio = n[0]
    gr = n[1]
    gpa = n[2]
    fio = fio.split()
    try:
        if len(fio) == 3:
            fio[0] = fio[0][0].upper() + fio[0][1:]
            fio[1] = fio[1][0].upper() + '.'
            fio[2] = fio[2][0].upper() + '.'
            fio = " ".join(fio)
        else:
            fio[0] = fio[0][0].upper() + fio[0][1:]
            fio[1] = fio[1][0].upper() + '.'
            fio = " ".join(fio)
        gr = 'гр. ' + gr
        gpa = 'GPA ' + str(round(gpa, 2)) + '0'
        return f'{fio}, {gr}, {gpa}'
    except:
        return 'TypeError'

def flattern(n):
    a = list()
    for i in n:
        if i.isdigit():
            a.append(i)
        if i.isalpha():
            return 'TypeError'
    return a

def count_freq(n):
    s = set(n)
    s = sorted((s))
    my_dic = {}
    for i in s:
        my_dic[i] = n.count(i)
    return my_dic

def top_n(n,b):
    s = count_freq(n)
    return list(s.items())[:b]

def col_sums(n):
    s = []
    als = []
    if len(n)==1:
        als.append(n[0][0])
        return als
    else:
        for x in range(len(n)-1):
            if len(n[x]) == len(n[x+1]):
                for y in range(len(n[0])):
                    s.append(n[x][y] + n[x+1][y])
            else:
                return 'ValueError'
        return s

