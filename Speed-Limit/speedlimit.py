x = 0
while True:
    x = int(input())
    if x == -1:
        break
    s = 0
    e = 0
    for i in range(x):
        a = input()
        b = a.split()
        c = int(b[0])
        d = int(b[1])
        s += c * (d - e)
        e = d
    print(s, "miles")
