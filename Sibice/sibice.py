import math

a = input()
b = a.split()
for i in range(int(b[0])):
    c = int(input())
    if (
        c <= int(b[1])
        or c <= int(b[2])
        or c <= int(math.sqrt(math.pow(int(b[1]), 2) + math.pow(int(b[2]), 2)))
    ):
        print("DA")
    else:
        print("NE")
