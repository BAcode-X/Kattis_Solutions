c = 0
for i in range(int(input())):
    b = input()
    c += int(b[:-1]) ** int(b[-1])
print(c)
