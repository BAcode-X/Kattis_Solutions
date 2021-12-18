g, s, c = [int(i) for i in input().split()]
buying = (g * 3) + (s * 2) + (c)
a = []
if buying >= 8:
    a.append("Province")
elif buying >= 5:
    a.append("Duchy")
elif buying >= 2:
    a.append("Estate")
if buying >= 6:
    a.append("Gold")
elif buying >= 3:
    a.append("Silver")
elif buying >= 0:
    a.append("Copper")
if len(a) == 1:
    print("".join(a))
else:
    print(str(a[0]), "or", str(a[1]))
