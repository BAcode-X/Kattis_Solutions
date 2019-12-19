a=int(input())
for i in range(a):
    b=input()
    c=b.split()
    d=int(c[0])
    e=int(c[1])
    f=int(c[2])
    if d==(e-f):
        print("does not matter")
    elif d>(e-f):
        print("do not advertise")
    else:
        print("advertise")
