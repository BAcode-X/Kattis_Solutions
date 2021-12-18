l = int(input())
d = int(input())
x = int(input())
a = []
for i in range(l, d + 1):
    k = sum([int(j) for j in str(i)])
    if k == x:
        a.append(i)
print(min(a))
prin
t(max(a))
