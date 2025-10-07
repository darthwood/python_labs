def row_sums(n):
    s = []
    for i in range(len(n)-1):
        if len(n[i]) == len(n[i+1]):
            s.append(sum(n[i]))
        else:
            raise 'ValueError'
    s.append(sum(n[-1]))
    return s

r1 = [[1, 2, 3], [4, 5, 6]]
r2 = [[-1, 1], [10, -10]]
r3 = [[0, 0], [0, 0]]
r4 = [[1, 2], [3]]

print(row_sums(r1))
print(row_sums(r2))
print(row_sums(r3))
print(row_sums(r4))

# src/lab02/matrix/row_sum.py
# [6, 6]
# [0, 0]
# [0, 0]
# ValueError