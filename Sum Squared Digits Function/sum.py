def nToB(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
a=int(input())
for i in range(a):
    b,c,d=[int(_)for _ in input().split()]
    e=nToB(d,c)
    cnt=0
    for j in e:
        cnt+=j**2
    print((i+1),cnt)
