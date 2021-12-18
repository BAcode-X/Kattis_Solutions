a = list(input())
vow = ["a", "e", "i", "o", "u"]
b = []
f = 0
for i in range(len(a)):
    if f:
        f -= 1
        continue
    if a[i] not in vow:
        b.append(a[i])
    else:
        b.append(a[i])
        f = 2
print("".join(b))
