from math import *

a = int(input())
for i in range(a):
    v, o, x, h1, h2 = [float(_) for _ in input().split()]
    r = (o * (3.1415)) / 180
    t = x / (v * cos(r))
    y = (v * t * sin(r)) - ((1 / 2) * (9.81) * (t ** 2))
    if y >= (h1 + 1) and y <= (h2 - 1):
        print("Safe")
    else:
        print("Not Safe")
