import math

x = int(input())
for i in range(x):
    a = input()
    b = list(a)
    c = int(math.sqrt(len(b)))
    r = c
    d = []
    for i in range(1, r + 1, +1):
        for j in range(1, r + 1, +1):
            d.append(b[c - i])
            c = c + r
        c = r
    print("".join(d))
