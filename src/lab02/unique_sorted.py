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

# src/lab02/unique_sorted.py
# 3, 1, 2, 1, 3
# [1, 2, 3]
#
#[]
#-1, -1, 0, 2, 2
#[-1, 0, 2]
# 1.0, 1, 2.5, 2.5, 0
# [0, 1, 2.5]