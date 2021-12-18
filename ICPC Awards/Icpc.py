a = int(input())
uni = []
team = []
for i in range(a):
    b = input().split()
    c = b[0]
    d = b[1]
    if c not in uni:
        uni.append(c)
        team.append(d)

for i in range(len(uni)):
    if i > 11:
        break
    else:
        print(uni[i], team[i])
