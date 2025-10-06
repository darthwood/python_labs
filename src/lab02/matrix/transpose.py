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

t1 = [[1, 2, 3]]
t2 = [[1], [2], [3]]
t3 = [[1, 2], [3, 4]]
t4 = []
t5 = [[1, 2], [3]]

print(transpose(t1))
print(transpose(t2))
print(transpose(t3))
print(transpose(t4))
print(transpose(t5))

# src/lab02/matrix/transpose.py
# [[1], [2], [3]]
# [[1, 2, 3]]
# [[1, 3], [2, 4]]
# []
# ValueError