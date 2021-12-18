import math

x, y = (int(i) for i in input().split())
z = math.ceil(x / (math.sin(math.radians(y))))
print(z)
