a=input().upper()
c=0
for i in range(len(a)):
    if i%3==0 and a[i]=="P":
        c+=1
    elif i%3==1 and a[i]=="E":
        c+=1
    elif i%3==2 and a[i]=="R":
        c+=1
print(len(a)-c)
