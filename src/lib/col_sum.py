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
                return 'ValueError'
        return s