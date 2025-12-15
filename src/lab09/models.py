from dataclasses import dataclass
from datetime import datetime, date
import re
import sys
import os

@dataclass
class Pervoxod:
    fio: str
    birth: str
    group: str
    gpa: float

    def __post_init__(self):
        self.prov_data()
        self.prov_gpa()

    def prov_data(self):
        pat = r'^\d{4}-\d{2}-\d{2}$'

        if not re.match(pat,self.birth):
            raise ValueError
        try:
            year, month, day = map(int, self.birth.split('-'))
            date(year,month,day)
        except ValueError:
            raise ValueError

    def prov_gpa(self):
        if not 0 <= self.gpa <= 5:
            raise ValueError

    def age(self) -> int:
        b_y, b_m, b_d = map(int, self.birth.split('-'))
        birthday = date(b_y,b_m,b_d)
        today = date.today()
        age = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1
        return age  

    def t_north(self) -> dict:
        return {
            'fio': self.fio,
            'birth': self.birth,
            'group': self.group,
            'gpa': self.gpa
        }  

    @classmethod
    def from_dict(cls, data: dict) -> 'Pervoxod':
        return cls(
            fio = data['fio'],
            birth = data['birth'],
            group = data['group'],
            gpa = data['gpa']
        )

    def __str__(self) -> str:
        return (f'Студент: {self.fio}\n'
                f'Дата рождения: {self.birth}\n'
                f'Группа: {self.group}\n'
                f'Средний балл: {self.gpa}\n'
                f'Возраст: {self.age()} лет')