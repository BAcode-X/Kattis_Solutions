a = int(input())
for i in range(a):
    b = input()
    c = input()
    d = list(b)
    e = list(c)
    f = []
    for j in range(len(d)):
        if d[j] == e[j]:
            f.append(".")
        else:
            f.append("*")
    g = "".join(f)
    print(b)
    print(c)
    print(g)
