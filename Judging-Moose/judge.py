a = input()
b = a.split()
c = int(b[0])
d = int(b[1])
if c == 0 and d == 0:
    print("Not a moose")
else:
    if c == d:
        print("Even", d * 2)
    elif c > d:
        print("Odd", c * 2)
    else:
        print("Odd", d * 2)
