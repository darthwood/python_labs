def flattern(n):
    a = list()
    for i in n:
        if i.isdigit():
            a.append(i)
        if i.isalpha():
            return 'TypeError'
    return a