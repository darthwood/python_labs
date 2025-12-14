import sys
import os
import json
from pathlib import Path
from models import Pervoxod
from typing import List
import argparse

def students_to_json(students: List[Pervoxod], path: str):
    vata = [shinoby.t_north() for shinoby in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(vata, f, ensure_ascii=False, indent=2)    

def students_from_json(path: str) -> List[Pervoxod]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            vata = json.load(f)
        tolpa = [Pervoxod.from_dict(zato) for zato in vata]
        return tolpa
    except FileNotFoundError:
        return 'JPA'
    
def print_students_info(students: List[Pervoxod], filename: str = ""):
    if not students:
        print("JPA")
        return 
    for student in students:
        print(f"Студент: {student.fio}, "
              f"Группа: {student.group}, "
              f"Возраст: {student.age()} лет, "
              f"Балл: {student.gpa}")   

def kava():
    banga = argparse.ArgumentParser(description='Сохранение/загрузка студентов JSON')
    
    banga.add_argument('--mode', type=str, required=True,
                        choices=['save', 'load'],
                        help='save: сохранить в JSON, load: загрузить из JSON')
    
    banga.add_argument('--input', type=str,
                        help='Входной JSON файл (для load)')
    
    banga.add_argument('--output', type=str,
                        help='Выходной JSON файл (для save)')
    
    banga.add_argument('--sample', action='store_true',
                        help='Использовать тестовых студентов (для save)')
    
    chaki = banga.parse_args()
    
    if chaki.mode == 'save':
        if chaki.sample and chaki.output:
            students = [
                Pervoxod("Иванов Иван Иванович", "2005-03-15", "SE-01", 4.8),
                Pervoxod("Петрова Анна Сергеевна", "2004-11-30", "SE-02", 3.5),
                Pervoxod("Сидоров Алексей Петрович", "2005-07-20", "SE-01", 2.9),
                Pervoxod("Кузнецова Мария Владимировна", "2004-05-10", "SE-03", 0.0)
            ]
            students_to_json(students, chaki.output)
    
    elif chaki.mode == 'load':
        if chaki.input:
            students = students_from_json(chaki.input)
            print_students_info(students, chaki.input)    

if __name__ == '__main__':
    kava()