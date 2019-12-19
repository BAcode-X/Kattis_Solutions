a=float(input())
b=int(input())
t=0
for i in range(b):
    x,y=[float(_) for _ in input().split()]
    t+=a*x*y
print("%.6f"%(t))
