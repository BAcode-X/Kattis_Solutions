a,b,c=[int(_)for _ in input().split()]
if b<a/2:
    b=a-b
if c<a/2:
    c=a-c
print(b*c*4)
