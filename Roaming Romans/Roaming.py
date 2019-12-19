a=float(input())
b=a*1000*(5280/4854)
if b>=(int(b)+0.5):
    print(int(b)+1)
else:
    print(int(b))
