a = int(input())
b = input()
c = b.split()
d, s = 0, 0
for i in range(len(c)):
    if c[i] == "-1":
        d += 1
    else:
        s += int(c[i])
print(s / (a - d))
