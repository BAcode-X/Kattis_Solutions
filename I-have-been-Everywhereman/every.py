a = int(input())
for i in range(a):
    b = int(input())
    c = []
    for i in range(b):
        d = input()
        if d not in c:
            c.append(d)
    print(len(c))
