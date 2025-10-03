def unique_sorted(n):
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
                return '[]'
    return sorted(set(m))

a = list(map(str, input().split(',')))
print(unique_sorted(a))