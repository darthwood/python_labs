def transpose(n):
    s = []
    for i in range(len(n)-1):
        if len(n[i]) != len(n[i+1]):
            return 'ValueError'
    if n == []:
        return []
    cls = len(n)
    rws = len(n[0])
    for x in range(rws):
        res = []
        for y in range(cls):
            res.append(n[y][x])
        s.append(res)
    return s