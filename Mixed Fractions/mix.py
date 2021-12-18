while True:
    a, b = [int(i) for i in input().split()]
    if a != 0 and b != 0:
        print(int(a / b), a % b, "/", b)
    else:
        break
