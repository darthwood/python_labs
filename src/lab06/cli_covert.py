import csv
import json
import sys 
import os
from openpyxl import Workbook
from pathlib import Path
import argparse

def csv_2_xlsx(puta: str|Path, outputa: str|Path = None, encoding='utf-8'):
    nig = Workbook()
    lis = nig.active
    lis.title = 'Девятихвостый Лис'

    if outputa is None:
        puta = Path(puta)
        diroputa = Path('data\output_stuff')
        outputa = diroputa / f'{puta.stem}.xlsx'


    with open(puta,'r',encoding='utf-8') as csv_fi:
        red = csv.reader(csv_fi)
        for nu_st, lin in enumerate(red,1):
            for nu_cmn, val in enumerate(lin,1):
                lis.cell(row=nu_st,column=nu_cmn,value=val)
    nig.save(outputa)  

def csv_2_json(puta: str|Path, outputa: str|Path = None, encoding='utf-8'):
    tester = []

    with open(puta, encoding='utf-8') as csv_fi:
        red = csv.DictReader(csv_fi)
        for li1 in red:
            tester.append(li1)
    
    if outputa is None:
        puta = Path(puta)
        diroputa = Path('data\output_stuff')
        outputa = diroputa / f'{puta.stem}.json'


    with open(outputa,'w',encoding='utf-8') as json_fi:
        json.dump(tester, json_fi, ensure_ascii=False, indent=2)


def json_2_csv(puta: str|Path, outputa: str|Path = None, encoding = 'utf-8'):
    with open(puta, 'r', encoding='utf-8') as json_fi:
        blue = json.load(json_fi)
    
    if outputa is None:
        puta = Path(puta)
        diroputa = Path('data\output_stuff')
        outputa = diroputa / f'{puta.stem}.csv'

    with open(outputa,'w',encoding='utf-8',newline='') as csv_fi:
        head = blue[0].keys()
        pisa = csv.DictWriter(csv_fi, fieldnames=head)
        pisa.writeheader()
        pisa.writerows(blue)    

def pyrga():
    pyrgen = argparse.ArgumentParser(description='Конвертер csv<=>json')
    pyrgen.add_argument('--mode',type=str,required=True,
                        choices=['csv2json','json2csv','csv2xlsx'],
                        help='Синяя пилюля или красная')
    pyrgen.add_argument('--input', type=str, required=True,
                        help='Вход в кроличью нору (типа: data.csv)')
    pyrgen.add_argument('--output', type=str,
                        help='Выход из кроличьей норы (Морфиус покажет, как она глубока)')
    pyrgen.add_argument('--encoding', type=str, default='utf-8',
                        help='Как читать эти символы (по умолчанию в ютф-8)')
    args = pyrgen.parse_args()
    if args.mode == 'csv2json':
        csv_2_json(args.input, args.output, args.encoding)

    elif args.mode == 'json2csv':
        json_2_csv(args.input, args.output, args.encoding)

    elif args.mode == 'csv2xlsx':
        csv_2_xlsx(args.input, args.output, args.encoding)    

if __name__=='__main__':
    pyrga()  

    # python src\\lab06\\cli_covert.py --mode csv2json --input data\\samples\\cities.csv --output data\\output_stuff\\megalodon.json