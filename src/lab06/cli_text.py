from pathlib import Path
import sys
import os
from umbapumpa import *
import argparse

tekst = input()
def cat(filey: str|Path, kol):
    if filey is Path:
        a = open(filey).readlines(int(kol))
        print(a)
    else:
        print(filey)

    


def kusak():
    kus = argparse.ArgumentParser(description='Обработчик текста')
    kus.add_argument('--mode', type=str, required= True,
                     choices= ['stats','cat'],
                     help='Выбор пилюли')
    kus.add_argument('--input', type=str, required=True,
                     help='Вводите аккуратно')
    kus.add_argument('--output', type=str, required=True,
                     help='Все, выносите')
    kus.add_argument('--encoding', type=str, required=True,
                     help='Вам на эльфийском?')
    barks = kus.parse_args()
    if barks.mode == 'stats':
        top_n(barks.input, barks.input, barks.output, barks.encoding)
    elif barks.mode == 'cat':

