from pathlib import Path
import csv

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

z = write_csv([('Привет',2), ('Мир',1), ('Суп','наварили')],'src/lab04/data.csv', ('Слово 1','значение 1'))             

s = open('src/lab04/data.csv','r',encoding='utf-8')
r = s.read()
print(r)
print(read_text('src/lab04/a.txt','utf-8'))

# src/lab04/io_txt_csv.py
# a,b
# Привет,2
# Мир,1
# Суп,наварили

# Привет, мир! Привет!!!
