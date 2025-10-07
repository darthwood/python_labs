def col_sums(n):
    s = []
    als = []
    if len(n)==1:
        als.append(n[0][0])
        return als
    else:
        for x in range(len(n)-1):
            if len(n[x]) == len(n[x+1]):
                for y in range(len(n[0])):
                    s.append(n[x][y] + n[x+1][y])
            else:
                raise 'ValueError'
        return s

c1 = [[1, 2, 3], [4, 5, 6]]
c2 = [[-1, 1], [10, -10]]
c3 = [[0, 0], [0, 0]]
c4 = [[1, 2], [3]]

print(col_sums(c1))
print(col_sums(c2))
print(col_sums(c3))
print(col_sums(c4))

# src/lab02/matrix/col_sum.py
# [5, 7, 9]
# [9, -9]
# [0, 0]
# ValueError