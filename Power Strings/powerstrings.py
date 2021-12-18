from math import *

while True:
    a = input()
    if a == ".":
        break
    m = -1
    for i in range(1, int(sqrt(len(a))) + 1):
        if len(a) % i == 0:
            if a[:i] * (len(a) // i) == a:
                m = max(m, (len(a) // i))
            if a[: (len(a) // i)] * i == a:
                m = max(m, i)
    print(m)
