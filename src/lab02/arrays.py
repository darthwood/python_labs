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

# src/lab02/arrays.py
# 3,-1,5,5,5,0
# (-1, 5)
# 42
# (42, 42)
# -5, -2, -9
# (-9, -2)
#[]
# ValueError
# 1.5, 2, 2.0, -3.1
# (-3.1, 2)