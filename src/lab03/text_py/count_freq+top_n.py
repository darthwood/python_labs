c1 = ["a","b","a","c","b","a"]
c2 = ["bb","aa","bb","aa","cc"]

def count_freq(n):
    s = set(n)
    s = sorted((s))
    my_dic = {}
    for i in s:
        my_dic[i] = n.count(i)
    return my_dic

def top_n(n,b):
    s = count_freq(n)
    return list(s.items())[:b]


print(count_freq(c1))
print(count_freq(c2))
# print(top_n(c1))
# print(top_n(c2))

# {'a': 3, 'b': 2, 'c': 1}
# {'aa': 2, 'bb': 2, 'cc': 1}
# [('a', 3), ('b', 2)]
# [('aa', 2), ('bb', 2)]