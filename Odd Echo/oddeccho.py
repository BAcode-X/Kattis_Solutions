a = [input() for i in range(int(input()))]
for i, j in enumerate(a):
    if not i % 2:
        print(j)