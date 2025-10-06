def row_sums(n):
    s = []
    for i in range(len(n)-1):
        if len(n[i]) == len(n[i+1]):
            s.append(sum(n[i]))
        else:
            return 'ValueError'
    s.append(sum(n[i]))
    return s