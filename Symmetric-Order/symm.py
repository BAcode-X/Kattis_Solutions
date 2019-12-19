c=1
while 1:
    a=int(input())
    if a==0:
        break
    b=[]
    d=[]
    for i in range(a):
        f=input()
        if i%2==0:
            b.append(f)
        else:
            d.append(f)
    e=b+d[::-1]
    print(f"SET {c}")
    for i in e:
        print(i)
    c+=1
