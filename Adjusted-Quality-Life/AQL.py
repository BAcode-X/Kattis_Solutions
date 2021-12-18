import math

a = int(input())
b = 0
for i in range(a):
    c, d = [float(_) for _ in input().split()]
    b += c * d
print("%.3f" % b)
