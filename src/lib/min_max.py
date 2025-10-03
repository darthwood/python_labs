def min_max(n):
    n = set(n)
    m = list()
    for i in n:
        try:
            if int(i) == float(i):
                m.append(int(i))
        except:
            try:
                m.append(float(i))
            except:
                return 'ValueError'
    return min(m),max(m)

n = list(map(str, input().split(',')))
print(min_max(n))