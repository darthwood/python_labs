def flattern(n):
    a = list()
    for i in n:
        if i.isdigit():
            a.append(i)
        if i.isalpha():
            raise 'TypeError'
    return a

n = list(map(str, input()))
print(flattern(n))

# src/lab02/flattern.py
# [[1, 2], [3, 4]]
# ['1', '2', '3', '4']
# [[1, 2], (3, 4, 5)]
# ['1', '2', '3', '4', '5']
# [[1], [], [2, 3]]
# ['1', '2', '3']
# [[1, 2], "ab"]
# TypeError