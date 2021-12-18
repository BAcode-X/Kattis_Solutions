x = input()
s = {"C": 0, "G": 0, "T": 0}
for i in x:
    s[i] += 1
y = 0
m = min(s.values())
for i in s:
    y += s[i] ** 2
y += 7 * m
print(y)
