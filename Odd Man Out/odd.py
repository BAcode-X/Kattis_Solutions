a = int(input())
for i in range(a):
    b = int(input())
    c = [int(_) for _ in input().split()]
    e = []
    for j in c:
        if j in e:
            e.remove(j)
        else:
            e.append(j)
    print(f"Case #{i+1}: {e[0]}")
