import math

x = int(input())
for i in range(x):
    a = int(input())
    b = str(math.factorial(a))
    print(b[-1])
