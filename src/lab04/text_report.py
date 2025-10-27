from pathlib import Path
from umbapumpa import *

s = read_text('src/lab04/a.txt','utf-8')
t = tokenize(s)
c = top_n(t,5)
i = write_csv(c,('src/lab04/report.csv'),('word','count'))
spice = open('src/lab04/report.csv','r',encoding='utf-8')
r = spice.read()
print(r)

# _labs/src/lab04/text_report.py
# word,count
# мир,1
# привет,2