n = int(input())

def ishashed(x):
    y = list(str(x))
    a =  eval('+'.join(y))
    if x % a == 0:
        return True
    return False

while 1:
    if ishashed(n):
        print(n)
        break
    n += 1

