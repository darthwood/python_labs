import csv
import json
import sys 
import importlib.util
file_path = 'src/lab05/json_csv.py'
spec = importlib.util.spec_from_file_location('json_csv',file_path)
con = importlib.util.module_from_spec(spec)
spec.loader.exec_module(con)
sys.modules['json_csv'] = con
from pathlib import Path
import argparse

def pyrga():
    pyrger = argparse.ArgumentParser(description='Конвертер csv<=>json')
    pyrger.add_argument('--mode',type=str,required=True,
                        choices=['csv2json','json2csv'],
                        help='Синяя пилюля или красная')
    pyrger.add_argument('--input', type=str, required=True,
                        help='Вход в кроличью нору (типа: data.csv)')
    pyrger.add_argument('--output', type=str,
                        help='Выход из кроличьей норы (Морфиус покажет, как она глубока)')
    pyrger.add_argument('--encoding', type=str, default='utf-8',
                        help='Как читать эти символы (по умолчанию в ютф-8)')
    args = pyrger.parse_args()
    if args.mode == 'csv2json':
        con.csv_2_json(args.input, args.output, args.encoding)

    elif args.mode == 'json2csv':
        con.json_2_csv(args.input, args.output, args.encoding)

if __name__=='__pyrga__':
    pyrga()          
