from pathlib import Path
import sys
import os
import argparse


def tokenize(n):
    import re
    n = n.casefold().strip()
    s = re.sub(r'[^0-9ёa-zA-Zа-яА-Я-]', ' ', n)
    s = s.replace('ё', 'е')
    s = s.split()
    s = ' '.join(s)
    return s.split(' ')

def count_freq(n):
    s = set(n)
    s = sorted((s))
    my_dic = {}
    for i in s:
        my_dic[i] = n.count(i)
    return my_dic


def chiko(filen, kol):
    with open(filen, 'r', encoding='utf-8') as f:
        a = f.read()
        t = sorted(tokenize(a))
        b = sorted(count_freq(t).items(),key=lambda item: item[1], reverse=True)[:kol]
    print(b)    
    
    
def cat(inputa, nado_li=False):
    with open(inputa, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        skoka_strok = len(str(len(lines)))
        for i, line in enumerate(lines, start=1):
            if nado_li:
                print(f"{i}. {line}",end='')
            else:
                print(line, end='')                



def kusak():
    kus = argparse.ArgumentParser(description='Обработчик текста')
    kus.add_argument('--mode', type=str, required= True,
                     choices= ['stats','cat'],
                     help='Выбор пилюли')
    kus.add_argument('--input', type=str, required=True,
                     help='Вводите аккуратно')
    kus.add_argument('--output', type=str,  #в коде нигде не реализован, просто есть и пусть будет
                     help='Все, выносите')
    kus.add_argument('--encoding', type=str, default='utf-8',
                     help='Вам на эльфийском?')
    kus.add_argument('-t','--top', type=int,
                     help='Для статс, показ лаптей')
    kus.add_argument('-n', '--number', action='store_true',
                     help='Циферизация строк')
    barks = kus.parse_args()
    if barks.mode == 'stats':
        chiko(barks.input, barks.top)
    elif barks.mode == 'cat':
        cat(barks.input, barks.number)

if __name__=='__main__':
    kusak()


#C:\Users\Andrew\HiGIT\python_labs> python .\src\lab06\cli_text.py --mode stats --input data\samples\chek.txt -t 5
#[('не', 2), ('тех', 2), ('чтобы', 2), ('я', 2), ('в', 1)]

# PS C:\Users\Andrew\HiGIT\python_labs> python .\src\lab06\cli_text.py --mode cat --input data\samples\chek.txt -n
# 1. Темный, мрачный коридор,
# 2. Я на цыпочках, как вор,
# 3. Пробираюсь, чуть дыша,
# 4. Чтобы не спугнуть
# 5. Тех, кто спит уже давно,
# 6. Тех, кому не все равно,
# 7. В чью я комнату тайком
# 8. Желаю заглянуть,
# 9. Чтобы увидеть...