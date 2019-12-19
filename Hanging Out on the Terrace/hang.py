a,b=[int(i)for i in input().split()]
c,g = 0,0
for i in range(b):
   d=input().split()
   if d[0] == "enter":
       if c+int(d[1]) <= a: c+=int(d[1])
       else: g+=1
   else:
        if c-int(d[1]) >= 0: c-=int(d[1])
        else: g+=1
print(g) 
