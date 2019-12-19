sum_x=0
ind=0
for i in range(1,6):
    a,b,c,d=[int(_) for _ in input().split()]
    s=a+b+c+d
    if s>sum_x:
        sum_x=s
        ind=i
print(ind,sum_x)
