def count_freq(n):
    s = set(n)
    s = sorted((s))
    my_dic = {}
    for i in s:
        my_dic[i] = n.count(i)
    return my_dic

def top_n(n):
    s = count_freq(n)
    return list(s.items())[:2]