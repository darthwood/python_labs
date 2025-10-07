def format_record(n):
    fio = n[0]
    gr = n[1]
    gpa = float(n[2])
    fio = fio.split()
    try:
        if len(fio) == 3:
            fio[0] = fio[0][0].upper() + fio[0][1:]
            fio[1] = fio[1][0].upper() + '.'
            fio[2] = fio[2][0].upper() + '.'
            fio = " ".join(fio)
        else:
            fio[0] = fio[0][0].upper() + fio[0][1:]
            fio[1] = fio[1][0].upper() + '.'
            fio = " ".join(fio)
        gr = 'гр. ' + gr
        gpa = 'GPA ' + str(round(gpa, 2)) + '0'
        return f'{fio}, {gr}, {gpa}'
    except:
        raise 'TypeError'

f1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
f2 = ("Петров Пётр", "IKBO-12", 5.0)
f3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
f4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
f5 = (' ',' ',456)
print(format_record(f1))
print(format_record(f2))
print(format_record(f3))
print(format_record(f4))
print(format_record(f5))

# src/lab02/format_record/format_record.py
# Иванов И. И., гр. BIVT-25, GPA 4.60
# Петров П., гр. IKBO-12, GPA 5.00
# Петров П. П., гр. IKBO-12, GPA 5.00
# Сидорова А. С., гр. ABB-01, GPA 4.00
# TypeError