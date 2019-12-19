x=input()
y=list(x)
p=['A','B','C']
c=1
for i in range(len(y)):
    if y[i]=='A':
        if c==1:
            c=2
        elif c==2:
            c=1
    elif y[i]=='B':
        if c==2:
            c=3
        elif c==3:
            c=2
    elif y[i]=='C':
        if c==1:
            c=3
        elif c==3:
            c=1
print(c)
