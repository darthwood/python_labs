import sys
import os
from dataclasses import dataclass
from datetime import datetime, date
from typing import List, Optional, Dict
from src.lab08.models import Pervoxod
from src.lab08.serialize import * #students_from_json, students_to_json, print_students_info
import argparse
import csv
import re
from pathlib import Path
from src.lab05.csv_xlsx import *
from src.lab05.json_csv import *

class Group:
    def __init__(self, debri: str):
        self.path = Path(debri)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True) 
            with open(self.path, 'w', encoding='utf-8', newline= '') as f:
                writer = csv.DictWriter(f, fieldnames=['fio','birth','group','gpa'])
                writer.writeheader()
            

    def _read_all(self):
        tolpa = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for x in reader:
                    tolpa.append(x)
        except Exception:
            print('Ошибочка вышла')
            return []
        return tolpa            
    

    def _write_all(self, tolpa: List[Dict]):
        
        print(f"\n Вызываю_write_all:")
        print(f"   Файл: {self.path.absolute()}")
        print(f"   Строк для записи: {len(tolpa)}")
    
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birth', 'group', 'gpa'])
                writer.writeheader()
                writer.writerows(tolpa)
        
            print(f"Получилось")
        
        
            print(f"\n Чек:")
            with open(self.path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)
        
        except Exception as e:
            print(f" Фигня какая-то: {e}")
            import traceback
            traceback.print_exc()
        
    def list(self) -> List[Pervoxod]:
        rows = self._read_all()
        tolpa = []
        for x in rows:
            try:
                if 'gpa' in x:
                    try:
                        x['gpa'] = float(x['gpa'])
                    except ValueError:
                        x['gpa'] = 0.0
                chui = Pervoxod.from_dict(x)
                tolpa.append(chui)
            except Exception:
                return ValueError
                continue
        return tolpa    

    def add(self, chui: Pervoxod):
        rows = self._read_all()
        for x in rows:
            if x['fio'] == chui.fio:
                print(f'Хата не резиновая')
                return
        new_row = {
            'fio': chui.fio,
            'birth': chui.birth,
            'group': chui.group,
            'gpa': str(chui.gpa)
        }
        rows.append(new_row)
        self._write_all(rows)
        print(f'Пихнул, да')

    def find(self, podstr: str) -> List[Pervoxod]:
        rows = self._read_all()
        find_rows = [r for r in rows if podstr.lower() in r['fio'].lower()]
        found_studs = []
        for x in find_rows:
            try:
                if 'gpa' in x:
                    try:
                        x['gpa'] = float(x['gpa'])
                    except ValueError:
                        x['gpa'] = 0.0    
                chui = Pervoxod.from_dict(x)
                found_studs.append(chui)  
            except Exception:
                return ValueError
                continue
        return found_studs

    def remove(self, fio: str) -> bool:
        rows = self._read_all()
        stacoun = len(rows)
        fio_normalized = ' '.join(fio.strip().split()).lower()
        rows = [
            r for r in rows
             if ' '.join(r['fio'].strip().split()).lower() != fio_normalized
             ]

        if len(rows) < stacoun:
            self._write_all(rows)
            print(f'В топку этого {fio}')
            return True
        else:
            print(f'Нет таких')
            return False


    def update(self, fio: str, **fields):
        print(f" Ищу этого добряка '{fio}'")
        print(f"   Поля для обновления: {fields}")
    
        rows = self._read_all()
    
        if not rows:
            print("Ниого немаэ")
            return
    
        print(f" Строк в файле: {len(rows)}")
    
        updated = False
        found_index = -1
    
        
        for i, row in enumerate(rows):
            print(f"   Проверка {i+1}: '{row['fio']}' == '{fio}'")
            if row['fio'] == fio:
                found_index = i
                print(f"Нашел на строке {i+1}!")
                break
    
        if found_index == -1:
            print(f"Чувак '{fio}' потерялся")
            print("\n Всего:")
            for i, row in enumerate(rows):
                print(f"   {i+1}. '{row['fio']}'")
            return
    
    
        old_data = rows[found_index].copy()
    
         
        if 'new_fio' in fields:
            rows[found_index]['fio'] = fields['new_fio']
            print(f"Обнулили: '{old_data['fio']}' → '{fields['new_fio']}'")
            
            del fields['new_fio']
    
    
        for field, value in fields.items():
            if field in rows[found_index]:
                
                if field == 'gpa':
                    rows[found_index][field] = str(value)
                else:
                     rows[found_index][field] = value
            
                print(f"✏️  {field}: '{old_data.get(field, 'N/A')}' → '{value}'")
    
        updated = True
    
    # Сохраняем
        if updated:
            print(f"\n Ща все будет")
            print(f"   Файл: {self.path}")
        
        # Покажем что будем сохранять
            print(f"\n Теперь вот так:")
            for i, row in enumerate(rows):
                if i == found_index:
                    print(f"   → {i+1}. {row['fio']} [Обнулен]")
                else:
                    print(f"   {i+1}. {row['fio']}")
        
        # ВЫЗЫВАЕМ СОХРАНЕНИЕ
            self._write_all(rows)
            print(f"Готово")
        else:
            print(f"Фигня какая-то, ничего не изменилось")

    def stats(self) -> Dict:
        tolpa = self.list()

        if not tolpa:
            return f'Здесь пусто'

        stats = {
            'Всего': len(tolpa),
            'Средний балл': sum(s.gpa for s in tolpa) / len(tolpa),
            'Средний возраст': sum(s.age() for s in tolpa) / len(tolpa),
            'Группы': sorted(set(s.group for s in tolpa)),
            'The Bestы': sum(1 for s in tolpa if s.gpa >= 4.5),
            'Нормисы': sum(1 for s in tolpa if s.gpa >= 3.5 and s.gpa < 4.5),
        }   

        return stats

    def show_girls(self):
        tolpa = self.list()
        
        if not tolpa:
            print('В околотке')
            return
        
        for i, chui in enumerate(tolpa, 1):
            print(f'\n#{i}: {chui.fio}')
            print(f'Дата рождения: {chui.birth}')
            print(f'Возраст: {chui.age()}')
            print(f'Группа: {chui.group}')
            print(f'Балл: {chui.gpa}')



def kava():
    banga = argparse.ArgumentParser(
        description='Работа со студентами: JSON, CSV, Group',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры:
  # Работа с JSON
  %(prog)s json --mode save --output students.json --sample
  %(prog)s json --mode load --input students.json
  
  # Работа с CSV (Group)
  %(prog)s csv --file students.csv --action list
  %(prog)s csv --file students.csv --action add --fio "Иванов" --birth "2005-03-15" --group "SE-01" --gpa 4.5
  
  # Конвертация
  %(prog)s convert --from students.csv --to students.json
  %(prog)s convert --from students.json --to students.csv
        """
    )
    

    subparsers = banga.add_subparsers(
        title="Режимы работы",
        dest="command",
        help="Выберите режим работы"
    )
    
    
    parser_json = subparsers.add_parser('json', help='Работа с JSON файлами')
    parser_json.add_argument('--mode', type=str, required=True,
                             choices=['save', 'load'],
                             help='save: сохранить, load: загрузить')
    parser_json.add_argument('--input', type=str, help='Входной JSON файл')
    parser_json.add_argument('--output', type=str, help='Выходной JSON файл')
    parser_json.add_argument('--sample', action='store_true',
                             help='Использовать тестовых студентов')
    
    
    parser_csv = subparsers.add_parser('csv', help='Работа с CSV файлами (Group)')
    parser_csv.add_argument('--file', type=str, required=True,
                            help='CSV файл группы')
    parser_csv.add_argument('--action', type=str, required=True,
                            choices=['list', 'add', 'find', 'remove', 'update', 'stats'],
                            help='Действие с группой')
    parser_csv.add_argument('--fio', type=str, help='ФИО студента')
    parser_csv.add_argument('--birth', type=str, help='Дата рождения (YYYY-MM-DD)')
    parser_csv.add_argument('--group', type=str, help='Группа')
    parser_csv.add_argument('--gpa', type=float, help='Средний балл (0-5)')
    parser_csv.add_argument('--search', type=str, help='Строка для поиска (для find)')
    parser_csv.add_argument('--new-fio', type=str, help='Новое ФИО (для update)')
    parser_csv.add_argument('--new-gpa', type=float, help='Новый средний балл (для update)')
    
    
    parser_convert = subparsers.add_parser('convert', help='Конвертация между форматами')
    parser_convert.add_argument('--from', type=str, required=True, dest='from_file',
                                help='Исходный файл')
    parser_convert.add_argument('--to', type=str, required=True,
                                help='Целевой файл')
    
    chaki = banga.parse_args()
    

    if not chaki.command:
        banga.print_help()
        return
    
    
    if chaki.command == 'json':
        if chaki.mode == 'save':
            if chaki.sample and chaki.output:
                students = [
                    Pervoxod("Иванов Иван Иванович", "2005-03-15", "SE-01", 4.8),
                    Pervoxod("Петрова Анна Сергеевна", "2004-11-30", "SE-02", 3.5),
                    Pervoxod("Сидоров Алексей Петрович", "2005-07-20", "SE-01", 2.9),
                    Pervoxod("Кузнецова Мария Владимировна", "2004-05-10", "SE-03", 0.0)
                ]
                students_to_json(students, chaki.output)
                print(f"Занесли {len(students)} студентов в {chaki.output}")
            elif not chaki.sample:
                print(" --sample!!!!!")
            elif not chaki.output:
                print("--output !!!!!!")
        
        elif chaki.mode == 'load':
            if chaki.input:
                students = students_from_json(chaki.input)
                print_students_info(students, chaki.input)
            else:
                print("Каков Ваш --input файл")
    
    
    elif chaki.command == 'csv':
        if not chaki.file:
            print("Где --file?")
            return
        
        group = Group(chaki.file)
        
        if chaki.action == 'list':
            students = group.list()
            if isinstance(students, list):
                if students:
                    print(f"\n Нашел {len(students)} студентов в файле {chaki.file}:")
                    for i, student in enumerate(students, 1):
                       print(f"\n#{i}: {student.fio}")
                       print(f"   Группа: {student.group}")
                       print(f"   Возраст: {student.age()} лет")
                       print(f"   Средний балл: {student.gpa}")
                else:
                    print(f"Файл {chaki.file} тупой и идет нафиг")
            else:
                print(f"Фигня получилась: функция вернула {type(students)} вместо списка")
                #print_students_info(students, chaki.file)
        
        elif chaki.action == 'add':
            if all([chaki.fio, chaki.birth, chaki.group, chaki.gpa]):
                try:
                    student = Pervoxod(chaki.fio, chaki.birth, chaki.group, chaki.gpa)
                    group.add(student)
                except Exception:
                    return ValueError
            else:
                print("Забыли про: --fio, --birth, --group, --gpa")
        
        elif chaki.action == 'find':
            if chaki.search:
                students = group.find(chaki.search)
                if isinstance(students, list):
                    if students:
                        print(f"\n Найдено {len(students)} студентов по запросу '{chaki.search}':")
                        for student in students:
                            print(f"  • {student.fio} (группа: {student.group}, GPA: {student.gpa})")
                else:
                    print(f"По запросу '{chaki.search}' ниче нет")
            else:
                print("--search надо")
        
        elif chaki.action == 'remove':
            if chaki.fio:
                group.remove(chaki.fio)
            else:
                print("--fio указывется чтобы затереть чувачка")
        
        elif chaki.action == 'update':
            if chaki.fio:
                fields = {}
                if chaki.new_fio:
                    fields['new_fio'] = chaki.new_fio
                if chaki.new_gpa:
                    fields['gpa'] = chaki.new_gpa
                if chaki.group:
                    fields['group'] = chaki.group
                if chaki.birth:
                    fields['birth'] = chaki.birth
                
                if fields:
                    group.update(chaki.fio, **fields)
                else:
                    print("Какие поля для обновления: --new-fio, --new-gpa, --group, --birth")
            else:
                print("укажите --fio студента, если он чето сменил")
        
        elif chaki.action == 'stats':
            stats = group.stats()
            print(f"\n📊 СТАТИСТИКА ГРУППЫ ({chaki.file}):")
            print(f"   Всего студентов: {stats['total']}")
            if stats['total'] > 0:
                print(f"   Средний балл: {stats['avg_gpa']:.2f}")
                print(f"   Средний возраст: {stats['avg_age']:.1f} лет")
                print(f"   Группы: {', '.join(stats['groups'])}")
    
    
    elif chaki.command == 'convert':
        from_ext = os.path.splitext(chaki.from_file)[1].lower()
        to_ext = os.path.splitext(chaki.to)[1].lower()
        
        if from_ext == '.csv' and to_ext == '.json':
            csv_2_json(chaki.from_file, chaki.to)
        elif from_ext == '.json' and to_ext == '.csv':
            json_2_csv(chaki.from_file, chaki.to)
        else:
            print(f"Тут так нету: {from_ext} → {to_ext}")
            print("   Поддерживается: CSV ↔ JSON")

if __name__ == '__main__':
    kava()