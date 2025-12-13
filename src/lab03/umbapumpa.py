from pathlib import Path
import csv
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

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    f_p = Path(path) #строка в path
    if not isinstance(path, str): 
        raise ValueError # чек что путь - строка
    if not f_p.exists():
        raise FileNotFoundError # есть ли файл
    try:
        with open(f_p, 'r', encoding=encoding) as file: # читаю файл
            con = file.read()
            return con
    except UnicodeDecodeError:
        raise UnicodeDecodeError    
    


def write_csv(rows, path, header=None):
    if rows is None:
        rows = [] # чек данных на входе, если ниче нет, то криейтим пустой
    if rows:# если там что-то есть, и строки одинаковой длины
        f_row_leng = len(rows[0])
        for i, row in enumerate(rows): # проверка энумерейтом по iндексам и значениям
            if len(row) != f_row_leng:  # чек что в роу в каждом блоке одинаковое кол-во данных
                raise ValueError
    if header and rows: # заголовок и входные тру
        if len(header) != len(rows[0]): #заголовков надо столько-же
            raise ValueError
    with open(path,'w',newline='',encoding='utf-8') as file: # пишем данные в табличку
        writer = csv.writer(file)
        if header is not None: # пишем заголовок
            writer.writerow(header)   
        for row in rows: # пишем строки
            writer.writerow(row) 


def chiko(filen, kol):
    with open(filen, 'r', encoding='utf-8') as f:
        a = f.read()
        t = sorted(tokenize(a))
        b = sorted(count_freq(t).items(),key=lambda item: item[1], reverse=True)[:kol]
    print(b)  
