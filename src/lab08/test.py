from models import Pervoxod
import sys
import os

novik = Pervoxod(
    fio = 'Иван Говнов',
    birth = '1972-04-14',
    group = 'БИВТ-25-8',
    gpa = 4.8
)

print(novik.birth)
print(novik.fio)
print(novik.age())