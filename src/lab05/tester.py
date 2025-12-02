from pathlib import Path
import sys
import os

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    f_p = Path(path) #строка в path
    if not isinstance(path, str): 
        raise ValueError # чек что путь - строка
    if not f_p.exists():
        raise FileNotFoundError # есть ли файл
    try:
        with open(f_p, 'r', encoding=encoding) as file: # читаю файл
            con = file.read()
            return con
    except UnicodeDecodeError:
        raise UnicodeDecodeError  

a = 'Устал кусать себя за локти' \
'я есть, я жив,' \
'я буду там'
# a = read_text('data\\samples\\chek.txt','utf-8')
print(read_text(a))

# number_lines = '-n' in sys.argv 
    
#     # Смотрим, есть ли имя файла среди параметров
#     filename = None
#     for arg in sys.argv[1:]:  # Перебираем все параметры кроме имени программы
#         if arg != '-n' and arg.endswith('.txt'):
#             filename = arg
#             break
    
#     if filename:
#         # 📁 СЛУЧАЙ 1: Читаем из файла
#         print(f"Читаем из файла: {filename}")
#         try:
#             # Открываем файл для чтения
#             with open(filename, 'r', encoding='utf-8') as file:
#                 text = file.read()
#             # Выводим текст
#             print_text(text, number_lines)
            
#         except FileNotFoundError:
#             print(f"Ошибка: файл '{filename}' не найден!")
#         except Exception as e:
#             print(f"Ошибка при чтении файла: {e}")
            
#     else:
#         # ⌨️ СЛУЧАЙ 2: Ввод с клавиатуры
#         print("Введите текст (для завершения введите пустую строку):")
#         lines = []
#         while True:
#             line = input()
#             if line == "":  # Если пустая строка - заканчиваем ввод
#                 break
#             lines.append(line)
        
#         # Объединяем все строки в один текст
#         text = '\n'.join(lines)
#         # Выводим текст
#         print_text(text, number_lines)

# # Запускаем программу
# if __name__ == "__main__":
#     main()