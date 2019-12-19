a=input()
b=a.split()
if int(b[1])>=45:
    b[1]=int(b[1])-45  
else:
    b[1]=60+(int(b[1])-45)
    if int(b[0])==0:
        b[0]=23
    else:
        b[0]=int(b[0])-1
c=tuple(b)
print(str(c[0])+" "+str(c[1]))
