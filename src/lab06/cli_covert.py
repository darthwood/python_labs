import csv
import json
import sys 
import os
from openpyxl import Workbook
from csv_xlsx import *
from json_csv import *
from pathlib import Path
import argparse

def pyrga():
    pyrger = argparse.ArgumentParser(description='Конвертер csv<=>json')
    pyrger.add_argument('--mode',type=str,required=True,
                        choices=['csv2json','json2csv','csv2xlsx'],
                        help='Синяя пилюля или красная')
    pyrger.add_argument('--input', type=str, required=True,
                        help='Вход в кроличью нору (типа: data.csv)')
    pyrger.add_argument('--output', type=str,
                        help='Выход из кроличьей норы (Морфиус покажет, как она глубока)')
    pyrger.add_argument('--encoding', type=str, default='utf-8',
                        help='Как читать эти символы (по умолчанию в ютф-8)')
    args = pyrger.parse_args()
    if args.mode == 'csv2json':
        csv_2_json(args.input, args.output, args.encoding)

    elif args.mode == 'json2csv':
        json_2_csv(args.input, args.output, args.encoding)

    elif args.mode == 'csv2xlsx':
        csv_2_xlsx(args.input, args.output, args.encoding)    

if __name__=='__main__':
    pyrga()  