a, b = [int(_) for _ in input().split()]
if a == b:
    print(a + 1)
elif a > b:
    for i in range(b, a + 1):
        print(i + 1)
else:
    for i in range(a, b + 1):
        print(i + 1)
