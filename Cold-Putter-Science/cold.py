x=int(input())
y=input()
f=y.split()
c=0
for i in range(len(f)):
    if int(f[i])<0:
        c+=1
print(c)
