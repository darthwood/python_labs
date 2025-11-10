from pathlib import Path
import csv 
from openpyxl import Workbook

def csv_2_xlsx(puta: str|Path, encoding='utf-8'):
    nig = Workbook()
    lis = nig.active
    lis.title = 'Девятихвостый Лис'

    with open(puta,'r',encoding='utf-8') as csv_fi:
        red = csv.reader(csv_fi)
        for nu_st, lin in enumerate(red,1):
            for nu_cmn, val in enumerate(lin,1):
                lis.cell(row=nu_st,column=nu_cmn,value=val)
    nig.save('src\lab05\ltabla.xlsx')  


an = csv_2_xlsx('src\lab05\pupa.csv',encoding='utf-8') 

