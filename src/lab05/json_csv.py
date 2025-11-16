from pathlib import Path
import json
import csv

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


# a = csv_2_json('src\lab04\data.csv',encoding='utf-8')
# b = json_2_csv('src\lab05\data.json',encoding='utf-8')   

# b = json_2_csv('src\lab05\data.json',encoding='utf-8') 
# Слово 1,значение 1
# Привет,2
# Мир,1
# Суп,наварили

# a = csv_2_json('src\lab04\data.csv',encoding='utf-8')
# [
#   {
#     "Слово 1": "Привет",
#     "значение 1": "2"
#   },
#   {
#     "Слово 1": "Мир",
#     "значение 1": "1"
#   },
#   {
#     "Слово 1": "Суп",
#     "значение 1": "наварили"
#   }
# ]

