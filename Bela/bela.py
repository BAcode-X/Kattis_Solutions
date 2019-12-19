dic={"A":(11,11),"K":(4,4),"Q":(3,3),"J":(20,2),"T":(10,10),"9":(14,0),"8":(0,0),"7":(0,0)}
a,b=[str(_)for _ in input().split()]
a=int(a)
cnt=0
for i in range(a*4):
    c=list(input())
    if c[1]==b:
        cnt+=dic[c[0]][0]
    else:
        cnt+=dic[c[0]][1]
print(cnt)
