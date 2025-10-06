def format_record(n):
    fio = n[0]
    gr = n[1]
    gpa = n[2]
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
        return 'TypeError'