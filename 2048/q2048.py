def fix(ls):
    a = [str(i) for i in ls if i!='0']
    for i in range(4):
        if i<len(a):
            ls[i]=a[i]
        else:
            ls[i]='0'
    return ls
def shift(ls):
    i = 0
    while i<3:
        ls = fix(ls)
        if ls[i]==ls[i+1] or ls[i]=='0':
            ls[i]=str(int(ls[i])+int(ls[i+1]))
            ls[i+1]='0'
        i+=1
    return fix(ls)

a = []
for i in range(4):
    b = [str(_)for _ in input().split()]
    a.append(b)
cmd = int(input())
c = []
if cmd % 2 == 0:
    for i in range(4):
        d = []
        if cmd == 0:
            d = shift(a[i])
        else:
            d = shift(a[i][::-1])
            d = d[::-1]
        c.append(d)
    for i in c:
        print(' '.join(i))
else:
    for i in range(4):
        d = []
        e = [j[i] for j in a]
        if cmd == 1:
            d = shift(e)
        else:
            d = shift(e[::-1])
            d = d[::-1]
        for j in range(4):
            a[j][i] = d[j]
    for i in a:
        print(' '.join(i))
    
    
